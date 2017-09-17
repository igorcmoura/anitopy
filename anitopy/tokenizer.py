# -*- coding: utf-8 -*-

import re

from anitopy.token import TokenCategory, TokenFlags, Token, Tokens


class Tokenizer:
    def __init__(self, filename, options):
        self.filename = filename
        self.options = options

    def tokenize(self):
        self._tokenize_by_brackets()
        return not Tokens.empty()

    def _add_token(self, category, content, enclosed):
        Tokens.append(Token(category, content, enclosed))

    def _tokenize_by_brackets(self):
        brackets = [
            ('(', ')'),  # U+0028-U+0029 Parenthesis
            ('[', ']'),  # U+005B-U+005D Square bracket
            ('{', '}'),  # U+007B-U+007D Curly bracket
            ('\u300C', '\u300D'),  # Corner bracket
            ('\u300E', '\u300F'),  # White corner bracket
            ('\u3010', '\u3011'),  # Black lenticular bracket
            ('\uFF08', '\uFF09'),  # Fullwidth parenthesis
        ]

        text = self.filename
        is_bracket_open = False
        matching_bracket = ''

        def find_first_bracket():
            open_brackets = [bracket_pair[0] for bracket_pair in brackets]

            index = next(
                (idx for idx, bracket in enumerate(text)
                 if bracket in open_brackets), -1)
            matching_bracket = next(
                (bracket_pair[1] for bracket_pair in brackets
                 if bracket_pair[0] == text[index]), None)
            return index, matching_bracket

        while text:
            if not is_bracket_open:
                bracket_index, matching_bracket = find_first_bracket()
            else:
                # Looking for the matching bracket allows us to better handle
                # some rare cases with nested brackets.
                bracket_index = text.find(matching_bracket)

            if bracket_index != 0:  # Found a token before the bracket
                self._tokenize_by_delimiters(
                    text[:bracket_index] if bracket_index != -1 else text,
                    is_bracket_open
                )

            if bracket_index != -1:  # Found bracket
                self._add_token(
                    TokenCategory.BRACKET, text[bracket_index], True)
                is_bracket_open = not is_bracket_open
                text = text[bracket_index+1:]
            else:  # Reached the end
                text = ''

    def _tokenize_by_delimiters(self, text, enclosed):
        pattern = '([{0}])'.format(self.options.allowed_delimiters)
        splited_text = re.split(pattern, text)

        for sub_text in splited_text:
            if sub_text:
                if sub_text in self.options.allowed_delimiters:
                    self._add_token(
                        TokenCategory.DELIMITER, sub_text, enclosed)
                else:
                    self._add_token(TokenCategory.UNKNOWN, sub_text, enclosed)

        self._validate_delimiter_tokens()

    def _validate_delimiter_tokens(self):
        def find_previous_valid_token(token):
            return Tokens.find_previous(token, TokenFlags.VALID)

        def find_next_valid_token(token):
            return Tokens.find_next(token, TokenFlags.VALID)

        def is_delimiter_token(token):
            return token is not None and \
                   token.category == TokenCategory.DELIMITER

        def is_unknown_token(token):
            return token is not None and \
                   token.category == TokenCategory.UNKNOWN

        def is_single_character_token(token):
            return is_unknown_token(token) and len(token.content) == 1 and \
                   token.content != '-'

        def append_token_to(token, append_to):
            append_to.content += token.content
            token.category = TokenCategory.INVALID

        for token in Tokens.get_list():
            if token.category != TokenCategory.DELIMITER:
                continue

            delimiter = token.content
            prev_token = find_previous_valid_token(token)
            next_token = find_next_valid_token(token)

            # Check for single-character tokens to prevent splitting group
            # names, keywords, episode number, etc.
            if delimiter != ' ' and delimiter != '_':
                if is_single_character_token(prev_token):
                    append_token_to(token, prev_token)
                    while is_unknown_token(next_token):
                        append_token_to(next_token, prev_token)
                        next_token = find_next_valid_token(next_token)
                        if is_delimiter_token(next_token) and \
                                next_token.content == delimiter:
                            append_token_to(next_token, prev_token)
                            next_token = find_next_valid_token(next_token)
                    continue
                if is_single_character_token(next_token):
                    append_token_to(token, prev_token)
                    append_token_to(next_token, prev_token)
                    continue

            # Check for adjacent delimiters
            if is_unknown_token(prev_token) and is_delimiter_token(next_token):
                next_delimiter = next_token.content
                if delimiter != next_delimiter and delimiter != ',':
                    if next_delimiter == ' ' or next_delimiter == '_':
                        append_token_to(token, prev_token)

            elif is_delimiter_token(prev_token) and \
                    is_delimiter_token(next_token):
                prev_delimiter = prev_token.content
                next_delimiter = next_token.content
                if prev_delimiter == next_delimiter and \
                        prev_delimiter != delimiter:
                    token.category = TokenCategory.UNKNOWN  # e.g. "&" in "_&_"

            # Check for other special cases
            if delimiter == '&' or delimiter == '+':
                if is_unknown_token(prev_token) and \
                        is_unknown_token(next_token):
                    if prev_token.content.isdigit() and \
                            next_token.content.isdigit():
                        append_token_to(token, prev_token)
                        append_token_to(next_token, prev_token)  # e.g. "01+02"

        Tokens.update([
            token for token in Tokens.get_list()
            if token.category != TokenCategory.INVALID
        ])

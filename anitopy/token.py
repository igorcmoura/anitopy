# -*- coding: utf-8 -*-

from enum import Enum


class TokenCategory(Enum):
    # Auto enumerate elements
    def __new__(cls):
        value = len(cls.__members__) + 1
        obj = object.__new__(cls)
        obj._value_ = value
        return obj

    UNKNOWN = ()
    BRACKET = ()
    DELIMITER = ()
    IDENTIFIER = ()
    INVALID = ()


class Token:
    def __init__(self, category=TokenCategory.UNKNOWN, content=None,
                 enclosed=False):
        self.category = category
        self.content = content
        self.enclosed = enclosed

    def __repr__(self):
        return 'Token(category = {0}, content = "{1}", enclosed = {2}'.format(
            self.category, self.content, self.enclosed
        )


def find_previous_token(tokens, token_index, category=None,
                        unwanted_categories=()):
    for token in tokens[token_index-1::-1]:
        if category and token.category != category:
            continue
        if token.category not in unwanted_categories:
            return token
    return None


def find_next_token(tokens, token_index, category=None,
                    unwanted_categories=()):
    for token in tokens[token_index+1:]:
        if category and token.category != category:
            continue
        if token.category not in unwanted_categories:
            return token
    return None

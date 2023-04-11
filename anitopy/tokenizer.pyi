# -*- coding: utf-8 -*-

from __future__ import annotations

from anitopy.anitopy import ParserOptions
from anitopy.element import Elements
from anitopy.token import TokenCategory, Tokens


class Tokenizer:
    filename: str
    options: ParserOptions
    elements: Elements
    tokens: Tokens

    def __init__(self, filename: str, options: ParserOptions, elements: Elements, tokens: Tokens) -> None: ...

    def tokenize(self) -> bool: ...

    def _add_token(self, category: TokenCategory, enclosed: bool = False) -> None: ...

    def _tokenize_by_brackets(self) -> None: ...

    def _tokenize_by_preidentified(self, text: str, enclosed: bool) -> None: ...

    def _tokenize_by_delimiters(self, text: str, enclosed: bool) -> None: ...

    def _validate_delimiter_tokens(self) -> None: ...

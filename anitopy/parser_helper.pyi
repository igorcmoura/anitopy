# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional

from anitopy.element import ElementCategory, Elements
from anitopy.token import Token, Tokens


def find_number_in_string(string: str) -> Optional[int]: ...


def find_non_number_in_string(string: str) -> Optional[int]: ...


def is_hexadecimal_string(string: str) -> bool: ...


def get_number_from_ordinal(string: str) -> Optional[str]: ...


def is_crc32(string: str) -> bool: ...


def is_dash_character(string: str) -> bool: ...


def is_latin_char(char: str) -> bool: ...


def is_mostly_latin_string(string: str) -> bool: ...


def is_resolution(string: str) -> bool: ...


def check_anime_season_keyword(elements: Elements, parsed_tokens: Tokens, token: str) -> bool: ...


def is_token_isolated(parsed_tokens: Tokens, token: Token) -> bool: ...


def build_element(
    elements: Elements, parsed_tokens: Tokens, category: ElementCategory,
    token_begin: Optional[Token] = None, token_end: Optional[Token] = None,
    keep_delimiters: bool = False
) -> bool: ...

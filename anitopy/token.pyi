# -*- coding: utf-8 -*-

from __future__ import annotations

from enum import Enum, IntFlag
from typing import Optional


class TokenCategory(Enum):
    UNKNOWN: int
    BRACKET: int
    DELIMITER: int
    IDENTIFIER: int
    INVALID: int


class TokenFlags(IntFlag):
    NONE: int
    BRACKET: int
    NOT_BRACKET: int
    DELIMITER: int
    NOT_DELIMITER: int
    IDENTIFIER: int
    NOT_IDENTIFIER: int
    UNKNOWN: int
    NOT_UNKNOWN: int
    VALID: int
    NOT_VALID: int

    ENCLOSED: int
    NOT_ENCLOSED: int

    MASK_CATEGORIES = \
        BRACKET | NOT_BRACKET | \
        DELIMITER | NOT_DELIMITER | \
        IDENTIFIER | NOT_IDENTIFIER | \
        UNKNOWN | NOT_UNKNOWN | \
        VALID | NOT_VALID

    MASK_ENCLOSED = ENCLOSED | NOT_ENCLOSED


class Token:
    category: TokenCategory
    content: Optional[str]
    enclosed: bool

    def __init__(
        self, category: TokenCategory = TokenCategory.UNKNOWN, content: Optional[str] = None, enclosed: bool = False
    ) -> None: ...

    def check_flags(self, flags: TokenFlags) -> bool: ...


class Tokens:
    _tokens: list[Token]

    def __init__(self) -> None: ...

    def empty(self) -> bool: ...

    def append(self, token: Token) -> None: ...

    def insert(self, index: int, token: Token) -> None: ...

    def update(self, tokens: list[Token]) -> None: ...

    def get(self, index: int) -> Token: ...

    def get_list(
        self, flags: Optional[TokenFlags] = None, begin: Optional[Token] = None, end: Optional[Token] = None
    ) -> list[Token]: ...

    def get_index(self, token: Token) -> int: ...

    def distance(self, token_begin: Token, token_end: Token) -> int: ...

    @staticmethod
    def _find_in_tokens(tokens: list[Token], flags: TokenFlags) -> Optional[Token]: ...

    def find(self, flags: TokenFlags) -> Optional[Token]: ...

    def find_previous(self, token: Optional[Token], flags: TokenFlags) -> Optional[Token]: ...

    def find_next(self, token: Optional[Token], flags: TokenFlags) -> Optional[Token]: ...

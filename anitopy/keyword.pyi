# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Optional

from anitopy.element import ElementCategory


class KeywordOption:
    identifiable: bool
    searchable: bool
    valid: bool

    def __init__(self, identifiable: bool = True, searchable: bool = True, valid: bool = True) -> None: ...


class Keyword:
    category: ElementCategory
    options: KeywordOption

    def __init__(self, category: ElementCategory, options: KeywordOption) -> None: ...


class KeywordManager:
    _file_extensions: dict[str, Keyword]
    _keys: dict[str, Keyword]

    def add(self, category: ElementCategory, options: KeywordOption, keywords: list[str]) -> None: ...

    def find(self, string: str, category: ElementCategory = ElementCategory.UNKNOWN) -> Optional[Keyword]: ...

    @staticmethod
    def peek(elements: list[str], string: str) -> list[tuple[int, int]]: ...

    @staticmethod
    def normalize(string: str) -> str: ...

    def _get_keyword_container(self, category: ElementCategory) -> dict[str, Keyword]: ...


keyword_manager: KeywordManager

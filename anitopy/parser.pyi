# -*- coding: utf-8 -*-

from __future__ import annotations

from anitopy.anitopy import ParserOptions
from anitopy.element import Elements
from anitopy.token import Tokens


class Parser:
    options: ParserOptions
    elements: Elements
    tokens: Tokens

    def __init__(self, options: ParserOptions, elements: Elements, tokens: Tokens) -> None: ...

    def parse(self) -> bool: ...

    def search_for_keywords(self) -> None: ...

    def search_for_isolated_numbers(self) -> None: ...

    def search_for_episode_number(self) -> None: ...

    def search_for_anime_title(self) -> None: ...

    def search_for_release_group(self) -> None: ...

    def search_for_episode_title(self) -> None: ...

    def validate_elements(self) -> None: ...

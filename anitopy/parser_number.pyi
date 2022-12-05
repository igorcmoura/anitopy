# -*- coding: utf-8 -*-

from __future__ import annotations

from typing import Literal

from anitopy.element import ElementCategory, Elements
from anitopy.token import Token, Tokens


ANIME_YEAR_MIN: Literal[1900]
ANIME_YEAR_MAX: Literal[2050]
EPISODE_NUMBER_MAX: Literal[1899]
VOLUME_NUMBER_MAX: Literal[20]


def str2int(string: str) -> int: ...


def is_valid_episode_number(number: str) -> bool: ...


def set_episode_number(elements: Elements, parsed_tokens: Tokens, token: Token, validate: bool) -> bool: ...


def set_alternative_episode_number(elements: Elements, number: str, token: Token) -> bool: ...


def check_extent_keyword(
    elements: Elements, parsed_tokens: Tokens, category: ElementCategory, token: Token
) -> bool: ...


def number_comes_after_prefix(
    elements: Elements, parsed_tokens: Tokens, category: ElementCategory, token: Token
) -> bool: ...


def number_comes_before_another_number(elements: Elements, parsed_tokens: Tokens, token: Token) -> bool: ...


def search_for_episode_patterns(elements: Elements, parsed_tokens: Tokens, tokens: list[str]) -> bool: ...


def match_single_episode_pattern(elements: Elements, word: str, token: str) -> bool: ...


def match_multi_episode_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_season_and_episode_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_type_and_episode_pattern(elements: Elements, parsed_tokens, Tokens, word: str, token: Token) -> bool: ...


def match_fractional_episode_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_partial_episode_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_number_sign_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_japanese_counter_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_episode_patterns(elements: Elements, parsed_tokens: Tokens, word: str, token: Token) -> bool: ...


def is_valid_volume_number(number: str) -> bool: ...


def set_volume_number(elements: Elements, number: str, token: Token, validate: bool) -> bool: ...


def match_single_volume_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_multi_volume_pattern(elements: Elements, word: str, token: Token) -> bool: ...


def match_volume_patterns(elements: Elements, word: str, token: Token) -> bool: ...


def set_season_number(elements: Elements, number: str, token: Token) -> bool: ...


def search_for_equivalent_numbers(elements: Elements, parsed_tokens: Tokens, tokens: list[Token]) -> bool: ...


def search_for_separated_numbers(elements: Elements, parsed_tokens: Tokens, tokens: list[Token]) -> bool: ...


def search_for_isolated_numbers(elements: Elements, parsed_tokens: Tokens, tokens: list[Token]) -> bool: ...


def search_for_last_number(elements: Elements, parsed_tokens: Tokens, tokens: list[Token]) -> bool: ...

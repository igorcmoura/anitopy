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


class Tokens:
    INSTANCE = None

    def __init__(self):
        self._tokens = []

    @classmethod
    def instance(cls):
        if not cls.INSTANCE:
            cls.INSTANCE = Tokens()
        return cls.INSTANCE

    @classmethod
    def clear(cls):
        del cls.INSTANCE
        cls.INSTANCE = None

    @classmethod
    def empty(cls):
        return len(cls.instance()._tokens) == 0

    @classmethod
    def append(cls, token):
        cls.instance()._tokens.append(token)

    @classmethod
    def update(cls, tokens):
        cls.instance()._tokens = tokens

    @classmethod
    def get_list(cls):
        return cls.instance()._tokens

    @classmethod
    def find_previous(cls, token_index, category=None, unwanted_categories=()):
        for token in cls.instance()._tokens[token_index-1::-1]:
            if category and token.category != category:
                continue
            if token.category not in unwanted_categories:
                return token
        return None

    @classmethod
    def find_next(cls, token_index, category=None, unwanted_categories=()):
        for token in cls.instance()._tokens[token_index+1:]:
            if category and token.category != category:
                continue
            if token.category not in unwanted_categories:
                return token
        return None

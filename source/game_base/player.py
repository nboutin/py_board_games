#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Player():

    def __init__(self, name, token, is_ai=False):
        self._name = name
        self._token = token
        self._is_ai = is_ai

    @property
    def name(self):
        return self._name

    @property
    def token(self):
        return self._token

    @property
    def is_ai(self):
        return self._is_ai

    @is_ai.setter
    def is_ai(self, val):
        self._is_ai = val

    def __str__(self):
        return self._name

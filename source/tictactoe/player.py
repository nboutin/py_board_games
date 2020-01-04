#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Player():

    def __init__(self, name, token):
        self._name = name
        self._token = token

    @property
    def name(self):
        return self._name

    @property
    def token(self):
        return self._token

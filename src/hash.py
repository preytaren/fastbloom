#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Singleton(type):
    _instance = None

    def __new__(mcs, name, *base, **attrs):
        if not mcs._instance:
            mcs._instance = type(name, *base, **attrs)
        return mcs._instance


# todo


class AbstrctHash(object):

    def __init__(self, prime):
        self._prime = prime

    def hash(self, keys):
        pass


class SpookyHash(AbstrctHash):

    def add_message(self, msg):
        pass

    def hash(self, keys):
        pass


class AdditiveHash(AbstrctHash):

    def __call__(self, keys):
        result = 0
        for key in keys:
            result += ord(key)
        return (result & 0xffffffff) % self._prime


class BKDRHash(AbstrctHash):

    SEED = 31

    def __call__(self, keys):
        _hash = 0
        for key in keys:
            _hash = _hash * self.SEED + ord(key)
        return (_hash & 0xffffffff) % self._prime


class MurmurHash(AbstrctHash):

    def hash(self, keys):
        pass


class city_hash(AbstrctHash):
    pass


class MurmurHashFactory(object):

    __metaclass__ = Singleton

    def get_orth_hashes(self, start, end, number=1):
        pass
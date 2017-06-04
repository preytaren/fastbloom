#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pyhash

from src.hash import *
from src.hash_tools import *


def _hash_test_helper(hash_func):
    r1 = hash_func('hello')
    assert isinstance(r1, int)
    assert 0 <= r1 <= 256
    r2 = hash_func('world')
    assert r1 != r2


def test_additive_hash():
    hash_obj = AdditiveHash(prime=128)
    _hash_test_helper(hash_obj)


def test_dbkr_hash():
    hash_obj = BKDRHash(prime=128)
    _hash_test_helper(hash_obj)


def test_murmur_hash():
    hash_obj = pyhash.mum_64()

def test_double_hashing():
    hash_func = double_hashing(5,
                               BKDRHash(128),
                               AdditiveHash(128))
    hash_func2 = double_hashing(3,
                                BKDRHash(128),
                                AdditiveHash(128))
    _hash_test_helper(hash_func)

    inputs = 'hello world'

    assert hash_func(inputs) != hash_func2(inputs)


def test_prime():
    for prime in primes():
        if prime < 1000:
            assert prime > 0
        else:
            break

#!/usr/bin/env python
# -*- coding: utf-8 -*-


def double_hashing_series(h1, h2, num_of_hashes):
    result = []
    for i in xrange(1, num_of_hashes+1):
        result.append(double_hashing(i, h1, h2))
    return result


def double_hashing(delta, h1, h2):
    """
    derive independant hash function based on hash function h1, h2
    :param delta: weight param in the double-hashing process
    :param h1: hash function
    :param h2: hash function
    :return: a new hash function equals h1 + delta * h2
    """
    def new_hash(msg):
        return h1(msg) + delta * h2(msg)
    return new_hash


def hashes(msg, h1, h2, number):
    h1_value, h2_value = h1(msg), h2(msg)
    for i in xrange(number):
        yield (h1_value + i*h2_value)

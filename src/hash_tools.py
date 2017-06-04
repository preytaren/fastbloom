#!/usr/bin/env python
# -*- coding: utf-8 -*-


def primes():
    prime_list, ve = [2], 3
    yield 2
    while True:
        for i in prime_list:
            if ve % i == 0:
                break
            elif i * i > ve + 1:
                yield ve
                prime_list.append(ve)
                break
        else:
            prime_list.append(ve)
            yield ve
        ve += 2


def double_hashing_series(h1, h2, num_of_hashes):
    count, prime_generator = 0, primes()
    result = []
    while count < num_of_hashes:
        result.append(double_hashing(prime_generator.send(None), h1, h2))
        count += 1
    return result


def double_hashing(delta, h1, h2):
    """
    derive independant hash function based on hash function h1, h2
    :param delta: weight param in the double-hashing process
    :param h1: hash function
    :param h2: hash function
    :return: a new hash function equals h1 + delta * h2
    """
    def new_hash(*args, **kwargs):
        return h1(*args, **kwargs) + delta * h2(*args, **kwargs)
    return new_hash

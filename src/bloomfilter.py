#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math, logging

import pyhash

from src.bitset import MmapBitSet
from src.hash_tools import double_hashing_series


class BloomFilter(object):
    """
    A bloom filter implementation,
    which use Murmur hash and Spooky hash
    """
    def __init__(self, input_size, acceptable_error_rate=0.001,
                 h1=pyhash.murmur3_x64_128(), h2=pyhash.spooky_128()):
        """

        :param input_size:
        :param acceptable_error_rate:
        :return:
        """
        # calculate m & k
        self._input_size = input_size
        self._num_of_bits, self._num_of_hash = self._adjust_param(4096*8,
                                                                  acceptable_error_rate)

        self._data_store = MmapBitSet(self._num_of_bits)
        self._size = len(self._data_store)
        self._hashes = double_hashing_series(h1,
                                             h2,
                                             self._num_of_hash)

    def _adjust_param(self, bits_size, expected_error_rate):
        """
        adjust k & m through 4 steps:
        1. Choose a ballpark value for n
        2. Choose a value for m
3       3. Calculate the optimal value of k
        4. Calculate the error rate for our chosen values of n, m, and k.
           If it's unacceptable, return to step 2 and change m;
           otherwise we're done.
        in every loop, m = m * 2
        :param bits_size:
        :param expected_error_rate:
        :return:
        """
        n, estimated_m, estimated_k, error_rate = self._input_size, int(bits_size/2), None, 1
        weight, e = math.log(2), math.exp(1)
        while error_rate > expected_error_rate:
            estimated_m *= 2
            estimated_k = int((float(estimated_m) / n) * weight) + 1
            error_rate = (1 - math.exp(- (estimated_k * n) / estimated_m)) ** estimated_k
            logging.info(estimated_m, estimated_k, error_rate)
        return estimated_m, estimated_k

    def add(self, msg):
        """
        add a string to bloomfilter
        :param msg:
        :return:
        """
        positions = []
        for _hash in self._hashes:
            positions.append(_hash(msg) % self._num_of_bits)
        for pos in sorted(positions):
            self._data_store.set(int(pos))

    def __contains__(self, msg):
        positions = []
        for hash in self._hashes:
            positions.append(hash(msg) % self._num_of_bits)
        for position in sorted(positions):
            if not self._data_store.test(position):
                return False
        return True



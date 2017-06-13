#!/usr/bin/env python
# -*- coding: utf-8 -*-
import math
import logging
import functools

import pyhash

from bitset import MmapBitSet
from hash_tools import hashes


class BloomFilter(object):
    """
    A bloom filter implementation,
    which use Murmur hash and Spooky hash
    """
    def __init__(self, capacity, error_rate=0.0001, fname=None,
                 h1=pyhash.murmur3_x64_128(), h2=pyhash.spooky_128()):
        """

        :param capacity: size of possible input elements
        :param error_rate: posi
        :param fname:
        :param h1:
        :param h2:
        """
        # calculate m & k
        self.capacity = capacity
        self.error_rate = error_rate
        self.num_of_bits, self.num_of_hashes = self._adjust_param(4096 * 8,
                                                                  error_rate)
        self._fname = fname
        self._data_store = MmapBitSet(self.num_of_bits)
        self._size = len(self._data_store)
        self._hashes = functools.partial(hashes, h1=h1, h2=h2, number=self.num_of_hashes)

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
        n, estimated_m, estimated_k, error_rate = self.capacity, int(bits_size / 2), None, 1
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
        if not isinstance(msg, str):
            msg = str(msg)
        positions = []
        for _hash_value in self._hashes(msg):
            positions.append(_hash_value % self.num_of_bits)
        for pos in sorted(positions):
            self._data_store.set(int(pos))

    @staticmethod
    def open(self, fname):
        with open(fname) as fp:
            raise NotImplementedError

    def __str__(self):
        """
        output bitset directly
        :return:
        """
        pass

    def __contains__(self, msg):
        if not isinstance(msg, str):
            msg = str(msg)
        positions = []
        for _hash_value in self._hashes(msg):
            positions.append(_hash_value % self.num_of_bits)
        for position in sorted(positions):
            if not self._data_store.test(position):
                return False
        return True

    def __len__(self):
        return self._size




#!/usr/bin/env python
# -*- coding: utf-8 -*-
from fastbloom.bitset import MmapBitSet


def test_mmap_bit_set_init():
    bset = MmapBitSet(1000)
    assert len(bset) == 4096 * 8

    bset = MmapBitSet(10000)
    assert len(bset) == 4096 * 8

    bset = MmapBitSet(100000)
    assert len(bset) == 4096 * 8 * 4


def test_mmap_bit_test_true():
    bset = MmapBitSet(1000)
    bset.set(1)
    assert bset.test(1) == True


def test_mmap_bit_test_false():
    bset = MmapBitSet(1000)
    bset.set(1)
    assert bset.test(2) == False


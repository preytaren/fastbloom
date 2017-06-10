#!/usr/bin/env python
# -*- coding: utf-8 -*-
import mmap, math


PAGE_SIZE = 4096
Byte_SIZE = 8
Byte_SIZE_SHIFT = 3


class MmapBitSet(object):

    def __init__(self, size):
        """
        Initialize a MmapBitSet,
        :param size: total bit in the set
        :return:
        """
        byte_size = ((size / 8) / PAGE_SIZE + 1) * PAGE_SIZE
        self._data_store = mmap.mmap(-1, byte_size)
        self._size = byte_size * 8

    def _write_byte(self, pos, byte):
        """
        write byte at pos
        :param pos: byte position
        :param byte: byte to write
        :return: None
        """
        self._data_store.seek(pos)
        self._data_store.write_byte(byte)

    def _read_byte(self, pos):
        """
        read byte at pos postion
        :param pos: byte position
        :return: ascii code of byte that read from datastore
        """
        self._data_store.seek(pos)
        return self._data_store.read_byte()

    def set(self, pos, val=True):
        """
        set bit at position "pos" to "val"
        :param pos: bit position to set
        :param val: value to set for the bit
        :return:
        """
        assert isinstance(pos, int)
        if pos < 0 or pos > self._size:
            raise ValueError('Invalid value bit {bit}, '
                             'should between {start} - {end}'.format(bit=pos,
                                                                     start=0,
                                                                     end=self._size))
        byte_no = pos >> Byte_SIZE_SHIFT
        inside_byte_no = pos % Byte_SIZE

        raw_byte = ord(self._read_byte(byte_no))
        if val:  # set to 1
            set_byte = raw_byte | (1 << inside_byte_no)
        else:  # set to 0
            set_byte = raw_byte & (1 << Byte_SIZE - 1 - 1 << inside_byte_no)
        if set_byte == raw_byte:
            return
        set_byte_char = chr(set_byte)
        self._write_byte(byte_no, set_byte_char)

    def test(self, pos):
        """
        test if a bit is set
        :param pos:
        :return: True if specified bit is set, otherwise False
        """
        byte_no = pos / Byte_SIZE
        inside_byte_no = pos % Byte_SIZE

        raw_byte = ord(self._read_byte(byte_no))
        bit = raw_byte & 2 ** inside_byte_no
        return True if bit else False

    def __len__(self):
        return self._size

    def __del__(self):
        self._data_store.close()


from fastbloom.bloomfilter import BloomFilter


def test_bloom_filter_init():
    bf = BloomFilter(1000, 0.001)
    # print bf._num_of_bits
    assert bf.num_of_bits % (4096 * 8) == 0
    assert bf.num_of_hashes == 23


def test_test_msg():
    bf = BloomFilter(30)
    msg = 'http://www.baidu.com'
    not_in_set_msg = 'http://www.google.com'

    bf.add(msg)

    assert msg in bf
    assert not_in_set_msg not in bf





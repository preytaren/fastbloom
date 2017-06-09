#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys, math, time

from src.bloomfilter import BloomFilter


def main(capacity=1000000, error_rate=0.0001):
    f = BloomFilter(capacity=capacity, error_rate=error_rate)

    print "Number of hashes:", f.num_of_hashes
    start = time.time()
    for i in xrange(0, f.capacity):
        f.add(i)
    end = time.time()
    print "{:5.3f} seconds to add to capacity, {:10.2f} entries/second".format(
        end - start, f.capacity / (end - start))

    print "Number of Filter Bits:{} ({} MB)".format(f.num_of_bits, f.num_of_bits/(8*1024*1024.0))
    print("------")

    # Look for false positive
    trials = f.capacity
    fp = 0
    start = time.time()
    for i in xrange(f.capacity, f.capacity + trials + 1):
        if i in f:
            fp += 1
    end = time.time()
    print(("{:5.3f} seconds to check false positives, "
           "{:10.2f} checks/second".format(end - start, trials / (end - start))))
    print("Requested FP rate: {:2.4f}".format(error_rate))
    print("Experimental FP rate: {:2.4f}".format(fp / float(trials)))
    # Compute theoretical fp max (Goel/Gupta)
    k = f.num_of_hashes
    m = f.num_of_bits
    n = f.capacity
    fp_theory = math.pow((1 - math.exp(-k * (n + 0.5) / (m - 1))), k)
    print("Projected FP rate (Goel/Gupta): {:2.6f}".format(fp_theory))


if __name__ == '__main__':
    main()

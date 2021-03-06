# Fastbloom
A lightweight but fast Bloomfilter written in Python(2.7).

# Introduction
Based on mmap and [MurMur](https://en.wikipedia.org/wiki/MurmurHash), [Spooky](http://burtleburtle.net/bob/hash/spooky.html) hash functions as the base
hashes. Use [double hashing](http://www.eecs.harvard.edu/~michaelm/postscripts/rsa2008.pdf) to reduce the number of hashes to two.

# Requirements
Install boost and boost-python
- Ubuntu
> sudo apt-get install libboost-all-dev

- Centos
> sudo yum install boost-devel

- OSX
> brew install boost boost-python

Install pyhash
> sudo pip install pyhash

Install fastbloom
> sudo pip install fastbloom

# Examples
```python
>>> from fastbloom import BloomFilter
>>> filter_ = BloomFilter(10000, 0.001) # set size of input 1000, error rate 0.1%
>>> filter_.add('www.google.com')
>>> 'www.google.com' in filter_
True
>>> 'www.github.com' in filter_
False
```
# Benchmark
When input_size set to 1000000, accepted_error_rate set to 0.01%
- Memory consumption: 4 MB
- Add operation: 7322.42 ops
- Check operation: 24788.79 ops
- Actual fault positive rate: 0.0000

You can just run the [benchmark.py](https://github.com/preytaren/pybloomfilter/blob/master/test/benchmarks.py) to see the actual benchmarks

# Todo
- add a faster bloomfilter
- add save and restore functions(as files)
- write a scalable bloomfilter

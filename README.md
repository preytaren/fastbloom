# pybloomfilter
A simple Bloomfilter written in Python(2.7).

# Introduction
Based on mmap and [MurMur](https://en.wikipedia.org/wiki/MurmurHash), [Spooky](http://burtleburtle.net/bob/hash/spooky.html) hash functions as the base
hashes.

# Requirements
Install boost and boost-python
- Ubuntu
> sudo apt-get install libboost-all-dev

- Centos
> sudo yum install boost-devel

- OSX
> brew install boost boost-python

Install pyhash
> pip install pyhash

# Examples
```python
>>> filter_ = Bloomfilter(1000, 0.001) # set size of input 1000, error rate 1%
>>> filter_.add('www.google.com')
>>> 'www.google.com' in filter_
True

>>> 'www.github.com' in filter_
False
```

# Todos
- add performance test
- write a scalable bloomfilter

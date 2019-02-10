from flatdict.flatdict import FlatDict
from random import randint


def repeat(s):
    return "{s}+{s}".format(s=s)


def get_rand(s):
    return randint(1, 1000000000)


def test_basic_flat_dict():
    fd = FlatDict(repeat)
    assert fd.ala == "ala+ala"


def test_caching():
    fd = FlatDict(get_rand)
    ala = fd.ala
    assert fd.ala == ala
    assert fd.ala != fd.beta


def test_cache_cleaning():
    fd = FlatDict(get_rand)
    ala1 = fd.ala
    ala2 = fd._.ala
    # Confirm cache has been refreshed.
    assert ala1 != ala2
    # Also the new value is cached.
    assert ala2 == fd.ala

from flatdict.flatdict import FlatDict


def test_basic_flat_dict():
    def repeat(s):
        return "{s}+{s}".format(s=s)

    fd = FlatDict(repeat)
    assert fd.ala == "ala+ala"
    assert 'ala' in fd.__dict__

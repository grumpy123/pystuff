import pytest
from tupplefactory.tuplefactory import tuple_factory, Required


def test_positionals():
    tc = tuple_factory('TC', tuple_req='a b c')
    tc1 = tc(1, 'blah', 3)
    assert tc1 is not None
    assert tc1.a == 1
    assert tc1.b == 'blah'
    assert tc1.c == 3


def test_kwargs():
    tc = tuple_factory('TC', tuple_req=['a', 'b', 'c'])
    tc1 = tc(a=1, b='foo', c=3)
    assert tc1 is not None
    assert tc1.a == 1
    assert tc1.b == 'foo'
    assert tc1.c == 3


def test_defaults():
    tc = tuple_factory('TC', a=Required, b=Required, c=4, d='foo')
    tc1 = tc(1, 'blah')
    assert tc1 is not None
    assert tc1.a == 1
    assert tc1.b == 'blah'
    assert tc1.c == 4
    assert tc1.d == 'foo'


def test_required():
    tc = tuple_factory('TC', tuple_req='a missing_b', c=4, d='foo')
    with pytest.raises(TypeError) as error_info:
        tc(1)
    assert 'missing_b' in str(error_info.value)


def test_required_kw():
    tc = tuple_factory('TC', a=Required, missing_b=Required, c=4, d='foo')
    with pytest.raises(TypeError) as error_info:
        tc(1)
    assert 'missing_b' in str(error_info.value)

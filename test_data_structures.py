import pytest

from easy_dict import EasyAccessDict, EasyDictError


def test_easy_dict():
    regular_dict = {'a': 1}
    easy_dict = EasyAccessDict(regular_dict)
    assert regular_dict['a'] == easy_dict.a
    with pytest.raises(EasyDictError) as e:
        easy_dict.b
        assert '"b"' in e

    regular_dict = {'a': 1, 'b': {'c': 2}}
    easy_dict = EasyAccessDict(regular_dict)
    assert regular_dict['a'] == easy_dict.a
    assert regular_dict['b']['c'] == easy_dict.b.c
    with pytest.raises(EasyDictError) as e:
        easy_dict.b.d
        assert '"d"' in e
    with pytest.raises(AttributeError):
        easy_dict.b.c.d

    regular_dict = {'a': 1, 'b': {'e': 1, 'c': [{'d': 2}]}}
    easy_dict = EasyAccessDict(regular_dict)
    assert regular_dict['a'] == easy_dict.a
    assert regular_dict['b']['e'] == easy_dict.b.e
    with pytest.raises(EasyDictError) as e:
        easy_dict.b.d
        assert '"d"' in e
    with pytest.raises(TypeError):
        easy_dict.b.c.d
    assert regular_dict['b']['c'][0]['d'] == easy_dict.b.c.first.d
    with pytest.raises(AttributeError):
        easy_dict.a.first
    with pytest.raises(EasyDictError):
        easy_dict.b.first
        assert '"first"' in e

    regular_dict = {1: '1'}
    easy_dict = EasyAccessDict(regular_dict)
    assert regular_dict[1] == easy_dict.get(1)

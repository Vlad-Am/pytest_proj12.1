from utils import dicts
import pytest


@pytest.fixture
def dicts_fixture():
    return {"a": 1, "b": 2}


def test_dicts(dicts_fixture):
    assert dicts.get_val(dicts_fixture, "a") == 1
    assert dicts.get_val(dicts_fixture, "a", "git") == 1
    assert dicts.get_val({}, "a", "git") == "git"
    assert dicts.get_val(dicts_fixture, "c", "git") == "git"

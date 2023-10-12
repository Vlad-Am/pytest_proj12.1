from utils import dicts


def test_dicts():
    assert dicts.get_val({"a": 1, "b": 2}, "a") == 1
    assert dicts.get_val({"a": 1, "b": 2}, "a", "git") == 1
    assert dicts.get_val({}, "a", "git") == "git"
    assert dicts.get_val({"a": 1, "b": 2}, "c", "git") == "git"

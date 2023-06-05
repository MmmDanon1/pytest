from tests.conftest import test_dict
from utils import dicts
def test_get_val(test_dict):
    assert dicts.get_val(test_dict, "vcs") == "mercurial"
    assert dicts.get_val(test_dict, 1) == "first"
    assert dicts.get_val({}, "vcs") == "git"
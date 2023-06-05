import pytest

@pytest.fixture
def test_dict():
    return {"vcs": "mercurial", 1: "first"}

@pytest.fixture
def test_slice_fixture():
    return [1, 2, 3, 4]
@pytest.fixture
def test_get_fixture():
    return [1, 2, 3]



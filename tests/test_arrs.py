from utils import arrs



def test_get(test_get_fixture):
    assert arrs.get(test_get_fixture, 1, "test") == 2
    assert arrs.get([], -1, "test") == "test"



def test_slice(test_slice_fixture):
    assert arrs.my_slice(test_slice_fixture, 1, 3) == [2, 3]
    assert arrs.my_slice(test_slice_fixture, 1) == [2, 3]
    assert arrs.my_slice([]) == []
    assert arrs.my_slice(test_slice_fixture, -1) == [4]
    assert arrs.my_slice(test_slice_fixture, -5) == [1, 2, 3, 4]



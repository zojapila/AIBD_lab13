from app import bubble_sort
import pytest

testdata = [[8,7,4,5,3,2,1,6], [6,5,4,3,2,1,7,8]]
@pytest.mark.parametrize('sample', testdata)
def test_bubble_sort(sample):
    expected = [1,2,3,4,5,6,7,8]
    got = bubble_sort(sample)
    assert expected == got
    
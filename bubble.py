
def bubble_sort(array):
    return array

def test_none():
    assert bubble_sort(None) is None

def test_empty():
    assert bubble_sort([]) == []

def test_one_element():
    assert bubble_sort([1]) == [1]

def test_1_2():
    assert bubble_sort([1,2]) == [1,2]

def test_2_1():
    assert bubble_sort([2,1]) == [1,2]
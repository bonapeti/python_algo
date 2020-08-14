from timeit import default_timer as timer
import pytest

def bubble_sort(array):
    
    if array is None:
        return None

    no_comparison = 0
    start = timer()

    for outer_index in range(0, len(array)):
        for inner_index in range(len(array) - 1, outer_index, -1):
            if (array[inner_index -1] > array[inner_index]):
                no_comparison = no_comparison + 1
                array[inner_index], array[inner_index -1] = array[inner_index - 1],array[inner_index]
    end = timer()
    print(end - start)
    print("Number of comparisons: {}".format(no_comparison))
    return array

def insertion_sort(array):
    if array is None:
        return None
    
    for outer_index in range(1, len(array)):
        current_value = array[outer_index]
        inner_index = outer_index - 1
        print("current_value={}, inner_index={}".format(current_value,inner_index))
        while current_value < array[inner_index] and inner_index >=0:
            array[inner_index + 1] = array[inner_index]
            inner_index = inner_index -1
            print("array={}".format(array))
        array[inner_index + 1] = current_value
        print("array={}".format(array))

    return array

def reversed_list(size):
    return list(range(size,0,-1))

def ordered_list(size):
    return list(range(1,size + 1))

@pytest.mark.parametrize("sort_fn, input,expected", [(bubble_sort, None, None), 
                                                    (bubble_sort, [],[]),
                                                    (bubble_sort, [1],[1]),
                                                    (bubble_sort, [3,2,1],[1,2,3]),
                                                    (insertion_sort,[],[]),
                                                    (insertion_sort,[1],[1]),
                                                    (insertion_sort,[3,2,1],[1,2,3])
                                                    ])
def test_sort(sort_fn, input, expected):
    assert sort_fn(input) == expected


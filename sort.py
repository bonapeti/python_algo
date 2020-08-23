from timeit import default_timer as timer
import pytest

def bubble_sort(array):
    if array is None:
        return None

    for outer_index in range(0, len(array)):
        for inner_index in range(len(array) - 1, outer_index, -1):
            if (array[inner_index -1] > array[inner_index]):
                array[inner_index], array[inner_index -1] = array[inner_index - 1],array[inner_index]
    return array

def insertion_sort(array):
    if array is None:
        return None
    
    for outer_index in range(1, len(array)):
        current_value = array[outer_index]
        inner_index = outer_index - 1
        while current_value < array[inner_index] and inner_index >=0:
            array[inner_index + 1] = array[inner_index]
            inner_index = inner_index -1
        array[inner_index + 1] = current_value

    return array

def selection_sort(array):



    for separator_index in range(len(array)):
        smallest, smallest_so_far_index = find_index_of_smallest(array[separator_index:len(array)])
        array[separator_index -1] 
        pass

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
                                                    (insertion_sort,[3,2,1],[1,2,3]),
                                                    (selection_sort,[3,2,1],[1,2,3])
                                                    ])
def test_sort(sort_fn, input, expected):
    assert sort_fn(input) == expected

@pytest.mark.parametrize("sort_fn, sizes", [(bubble_sort, [10,100,1000,10000]), 
                                            (insertion_sort,[10,100,1000,10000])
                                                    ])
def te1st_performance(sort_fn, sizes):
    for size in sizes:
        start = timer()
        sort_fn(reversed_list(size))
        end = timer()
        print("Sorting with {} of size {} took {}".format(sort_fn,size, end - start))
from timeit import default_timer as timer
import pytest
import sys

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

    def find_smallest_element(array):
        smallest_so_far = sys.maxint
        smallest_index = -1
        for index, value in enumerate(array):
            if value < smallest_so_far:
                smallest_so_far = value
                smallest_index = index
        return smallest_index, smallest_so_far

    for separator_index in range(len(array)):
        smallest_so_far_index, smallest = find_smallest_element(array[separator_index:len(array)])
        if smallest_so_far_index != -1:
            for swapping_index in range(smallest_so_far_index,0,-1):
                real_swapping_index = swapping_index + separator_index
                array[real_swapping_index] = array[real_swapping_index-1]
            array[separator_index] = smallest

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
                                                    (selection_sort,[3,2,1],[1,2,3]),
                                                    (selection_sort,[11, 25, 12, 22, 64],[11,12,22, 25, 64])
                                                    ])
def test_sort(sort_fn, input, expected):
    assert sort_fn(input) == expected

@pytest.mark.parametrize("sort_fn, sizes", [(bubble_sort, [10,100,1000,10000]), 
                                            (insertion_sort,[10,100,1000,10000]),
                                            (selection_sort,[10,100,1000,10000])
                                                    ])
def test_performance(sort_fn, sizes):
    for size in sizes:
        start = timer()
        sort_fn(reversed_list(size))
        end = timer()
        print("Sorting with {} of size {} took {}".format(sort_fn,size, end - start))
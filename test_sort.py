import pytest
from timeit import default_timer as timer
from sort import bubble_sort
from sort import insertion_sort
from sort import selection_sort

def reversed_list(size):
    return list(range(size,0,-1))



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
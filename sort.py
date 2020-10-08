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
        smallest_so_far = sys.maxsize
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

def merge_sort(array):

    if array is None:
        return None

    if len(array) < 2:
        return array


    def next_or_infinite(array,i):
        if i < len(array):
            return array[i]
        else:
            return sys.maxsize

    

    divisor = int(len(array) / 2)
    left_array = array[:divisor]
    right_array = array[divisor:]
    merge_sort(left_array)
    merge_sort(right_array)
    
    left_index = 0
    right_index = 0
    for i in range(len(array)):
        
        if next_or_infinite(left_array,left_index) < next_or_infinite(right_array,right_index):
            array[i] = next_or_infinite(left_array,left_index)
            left_index = left_index + 1
        else:
            array[i] = next_or_infinite(right_array,right_index)
            right_index = right_index + 1

    return array
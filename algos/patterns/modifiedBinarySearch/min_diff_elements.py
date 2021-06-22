# Given an array of numbers sorted in ascending order, find the element in the array that has the minimum difference with the given ‘key’.

# Example 1:

# Input: [4, 6, 10], key = 7
# Output: 6
# Explanation: The difference between the key '7' and '6' is minimum than any other number in the array 
# Example 2:

# Input: [4, 6, 10], key = 4
# Output: 4
# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: 10
# Example 4:

# Input: [4, 6, 10], key = 17
# Output: 10
import math

def search_min_diff_element(arr, key):
    '''
    TC : O(LogN)
    SC: O(1)
    '''
    start = 0
    end = len(arr) - 1


    if arr[end] < key:
        return arr[end]

    while start <= end:
        mid = (start + end)//2
        if arr[mid] == key:
            return arr[mid]

        if arr[mid] > key:
            end = start - 1
        else:
            start = mid + 1
    

    if arr[start] - key > arr[end] - key:
        return arr[end]
    return arr[start]


if __name__ == '__main__':
    r1 = (search_min_diff_element([4, 6, 10], 7))
    r2 = (search_min_diff_element([4, 6, 10], 4))
    r3 = (search_min_diff_element([1, 3, 8, 10, 15], 12))
    r4 = (search_min_diff_element([4, 6, 10], 10))

    print(r1)
    print(r2)
    print(r3)
    print(r4)

    assert r1 == 6
    assert r2 == 4
    assert r3 == 10
    assert r4 == 10


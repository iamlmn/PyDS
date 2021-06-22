# Given an array of numbers which is sorted in ascending order and is rotated ‘k’ times around a pivot, find ‘k’.

# You can assume that the array does not have any duplicates.

# Example 1:

# Input: [10, 15, 1, 3, 8]
# Output: 2
# Explanation: The array has been rotated 2 times.


def get_rotation_count(array):
    s = 0 
    e = len(array) - 1

    while s <= e: 
        m = (s + e)//2  
        if array[m] >= array[s]:
            s = m + 1
        else:
            e = m - 1
    return s % len(array)

if __name__ == '__main__':
    arr1 = [10, 15, 1, 3, 8]
    arr2 = [4, 5, 7, 9, 10, -1, 2]
    arr3 = [1, 3, 8, 10]

    r1 = get_rotation_count(arr1)
    r2 = get_rotation_count(arr2)
    r3 = get_rotation_count(arr3)

    print(r1) 
    print(r2)
    print(r3)

    assert r1 == 2
    assert r2 == 5
    assert r3 == 0
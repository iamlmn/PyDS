# Given an array of numbers which is sorted in ascending order and also rotated by some arbitrary number, 
# find if a given ‘key’ is present in it.

# Write a function to return the index of the ‘key’ in the rotated array. If the ‘key’ is not present, return -1. 
# You can assume that the given array does not have any duplicates.

# Example 1:

# Input: [10, 15, 1, 3, 8], key = 15
# Output: 1
# Explanation: '15' is present in the array at index '1'.


# Example 2:

# Input: [4, 5, 7, 9, 10, -1, 2], key = 10
# Output: 4
# Explanation: '10' is present in the array at index '4'.


def search_rotated_array(array, key):
    s = 0
    e = len(array) - 1

    while s <= e:
        m = (s + e) // 2

        if array[m] == key:
            return m
        elif array[m] >= array[s]:
            if key < array[m] and key >= array[s]:
                e = m - 1
            else:
                s = m + 1
        else:
            if key > array[m] and key <= array[e]:
                s = m + 1
            else:
                e = m - 1

    return -1


if __name__ == '__main__':
    arr1 = [10, 15, 1, 3, 8]
    key1 = 15

    arr2 = [4, 5, 7, 9, 10, -1, 2]
    key2 = 10

    r1 = search_rotated_array(arr1, key1)
    r2 = search_rotated_array(arr2, key2)

    print(r1, r2)

    assert r1 == 1
    assert r2 == 4

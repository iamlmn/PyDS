# Given a sorted array, create a new array containing squares of all the number of the input array in the sorted order.

# Example 1:

# Input: [-2, -1, 0, 2, 3]
# Output: [0, 1, 4, 4, 9]
# Example 2:

# Input: [-3, -1, 0, 1, 2]
# Output: [0 1 1 4 9]


def sortedArray(array):
    i = 0
    j = len(array) - 1
    sortedArray = []

    while i <= j:
        if abs(array[i]) >= abs(array[j]):
            sortedArray.append(array[i] * array[i])
            i += 1
        else:
            sortedArray.append(array[j] * array[j])
            j -= 1

    return sortedArray[:: -1]


if __name__ == '__main__':
    nums1 = [-2, -1, 0, 2, 3]
    nums2 = [-3, -1, 0, 1, 2]
    x1 = sortedArray(nums1)
    assert x1 == [0, 1, 4, 4, 9]
    print(x1)

    x2 = sortedArray(nums2)
    assert x2 == [0, 1, 1, 4, 9]
    print(x2)
 
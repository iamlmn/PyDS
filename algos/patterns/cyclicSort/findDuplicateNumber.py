# We are given an unsorted array containing ‘n+1’ numbers taken from the range 1 to ‘n’. 
# The array has only one duplicate but it can be repeated multiple times. 
# Find that duplicate number without using any extra space. You are, however, allowed to modify the input array.

# Example 1:

# Input: [1, 4, 4, 3, 2]
# Output: 4
# Example 2:

# Input: [2, 1, 3, 3, 5, 4]
# Output: 3
# Example 3:

# Input: [2, 4, 1, 4, 4]
# Output: 4

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def findMissingNumber(array):
    i = 0
    n = len(array)

    while i < n:
        if array[i] != i + 1:
            if array[i] != array[array[i] - 1]:
                swap(i, array[i] - 1, array)
            else:
                return array[i]

        else:
            i += 1

    return -1

if __name__ == '__main__':
    array1 = [1, 4, 4, 3, 2]
    array2 = [2, 1, 3, 3, 5, 4]
    array3 = [2, 4, 1, 4, 4]

    out1 = 4
    out2 = 3
    out3 = 4

    r1 = findMissingNumber(array1)
    r2 = findMissingNumber(array2)
    r3 = findMissingNumber(array3)

    print(r1)
    print(r2)
    print(r3)
    assert out1 == r1
    assert out2 == r2
    assert out3 == r3

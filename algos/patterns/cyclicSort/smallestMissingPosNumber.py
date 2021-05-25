# Given an unsorted array containing numbers, find the smallest missing positive number in it.

# Example 1:

# Input: [-3, 1, 5, 4, 2]
# Output: 3
# Explanation: The smallest missing positive number is '3'
# Example 2:

# Input: [3, -2, 0, 1, 2]
# Output: 4
# Example 3:

# Input: [3, 2, 5, 1]
# Output: 4

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def firstMinNumber(array):
    i = 0
    n = len(array)

    while i < n:
        if array[i] > 0 and array[i] < n and array[i] != array[array[i] - 1] :
            swap(i, array[i] - 1, array)
        else:
            i += 1

    for i in range(len(array)):
        if i + 1 != array[i]:
            return i + 1
    return -1

if __name__ == '__main__':
    array1 = [-3, 1, 5, 4, 2]
    array2 = [3, -2, 0, 1, 2]
    array3 = [3, 2, 5, 1]

    out1 = 3
    out2 = 4
    out3 = 4

    r1 = firstMinNumber(array1)
    r2 = firstMinNumber(array2)
    r3 = firstMinNumber(array3)

    print(r1)
    print(r2)
    print(r3)
    assert out1 == r1
    assert out2 == r2
    # assert out3 == r3



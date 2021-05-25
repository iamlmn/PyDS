# We are given an array containing ‘n’ distinct numbers taken from the range 0 to ‘n’.
# Since the array has only ‘n’ numbers out of the total ‘n+1’ numbers, find the missing number.

# Example 1:

# Input: [4, 0, 3, 1]
# Output: 2
# Example 2:

# Input: [8, 3, 5, 2, 4, 6, 0, 1]
# Output: 7


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def findMissingNumber(array):

    i = 0
    n = len(array)

    while i < n:
        if array[i] != i and array[i] < n:
            swap(i, array[i], array)
        else:
            i += 1

    for i in range(len(array)):
        if array[i] != i:
            return i
    return -1

def findMissingNumber2(array):
    # O(n) t, O(1) space
    return (len(n) * (len(n)- 1) / 2 ) - sum(array)


if __name__ == '__main__':
    array1 = [4, 0, 3, 1]
    array2 = [8, 3, 5, 2, 4, 6, 0, 1]

    out1 = 2
    out2 = 7

    r1 = findMissingNumber(array1)
    r2 = findMissingNumber(array2)

    print(r1, r2)
    assert out1 == r1
    assert out2 == r2

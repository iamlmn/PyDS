# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. The array has some duplicates, find all the duplicate numbers without using any extra space.

# Example 1:

# Input: [3, 4, 4, 5, 5]
# Output: [4, 5]
# Example 2:

# Input: [5, 4, 7, 2, 3, 5, 3]
# Output: [3, 5]


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def findDuplicates(array):
    i = 0
    n  = len(array)
    duplicates = []
    while i < n:
        if array[i] != i + 1:
            if array[i] == array[array[i] - 1]:
                if array[i] not in duplicates:
                    duplicates.append(array[i])
                i += 1
                continue
            else:
                swap(i, array[i] - 1, array)
        else:
            i += 1
    # sort(duplicae/)
    return sorted(duplicates)


if __name__ == '__main__':
    array1 = [3, 4, 4, 5, 5]
    array2 = [5, 4, 7, 2, 3, 5, 3]
    # array3 = [2, 4, 1, 4, 4]

    out1 = [4, 5]
    out2 = [3, 5]
    # out3 = 4

    r1 = findDuplicates(array1)
    r2 = findDuplicates(array2)
    # r3 = findMissingNumber(array3)

    print(r1)
    print(r2)
    # print(r3)
    assert out1 == r1
    assert out2 == r2
    # assert out3 == r3


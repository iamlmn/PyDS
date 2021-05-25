# We are given an unsorted array containing ‘n’ numbers taken from the range 1 to ‘n’. 
# The array originally contained all the numbers from 1 to ‘n’, but due to a data error, 
# one of the numbers got duplicated which also resulted in one number going missing. Find both these numbers.

# Example 1:

# Input: [3, 1, 2, 5, 2]
# Output: [2, 4]
# Explanation: '2' is duplicated and '4' is missing.
# Example 2:

# Input: [3, 1, 2, 3, 6, 4]
# Output: [3, 5]
# Explanation: '3' is duplicated and '5' is missing.

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def getCorruptedData(array):
    i = 0
    n = len(array)
    res = [-1, -1]
    while i < n:
        if array[i] != array[array[i] - 1]:
            swap(i, array[i] - 1, array)
        else:
            i += 1

    for i in range(len(array)):
        if i + 1 != array[i]:
            res =[ array[i], i + 1]
    
    return res

if __name__ == '__main__':
    array1 = [3, 1, 2, 5, 2]
    array2 = [3, 1, 2, 3, 6, 4]
    # array3 = [2, 4, 1, 4, 4]

    out1 = [2, 4]
    out2 = [3, 5]
    # out3 = 4

    r1 = getCorruptedData(array1)
    r2 = getCorruptedData(array2)
    # r3 = findMissingNumber(array3)

    print(r1)
    print(r2)
    # print(r3)
    assert out1 == r1
    assert out2 == r2
    # assert out3 == r3



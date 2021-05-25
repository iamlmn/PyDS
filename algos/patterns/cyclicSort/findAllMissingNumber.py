# We are given an unsorted array containing numbers taken from the range 1 to ‘n’. 
# The array can have duplicates, which means some numbers will be missing. Find all those missing numbers.

# Example 1:

# Input: [2, 3, 1, 8, 2, 3, 5, 1]
# Output: 4, 6, 7
# Explanation: The array should have all numbers from 1 to 8, due to duplicates 4, 6, and 7 are missing.

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]

def findDuplicates(array):
    duplicates = []
    missingNumber = []
    i = 0
    n = len(array)
    while i < n:
        if array[i] != i + 1:
            if array[i] == array[array[i] - 1]:
                # print(f"Duplicate at {i} : {array[i]}")
                duplicates.append(array[i])
                i += 1
                continue
            swap(i, array[i] - 1, array)
        else:
            
            i += 1
    for i in range(len(array)):
        if i + 1 != array[i]:
            missingNumber.append(i + 1)
    return missingNumber
if __name__ == '__main__':
    array1 = [2, 3, 1, 8, 2, 3, 5, 1]
    array2 = [2, 4, 1, 2]
    array3 = [2, 3, 2, 1]

    out1 = [4, 6, 7]
    out2 = [3]
    out3 = [4]

    r1 = findDuplicates(array1)
    r2 = findDuplicates(array2)
    r3 = findDuplicates(array3)

    print(r1)
    print(r2)
    print(r3)
    assert out1 == r1
    assert out2 == r2
    assert out3 == r3

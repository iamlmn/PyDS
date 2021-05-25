# Find the First K Missing Positive Numbers (hard) #
# Given an unsorted array containing numbers and a number ‘k’, find the first ‘k’ missing positive numbers in the array.

# Example 1:

# Input: [3, -1, 4, 5, 5], k=3
# Output: [1, 2, 6]
# Explanation: The smallest missing positive numbers are 1, 2 and 6.
# Example 2:

# Input: [2, 3, 4], k=3
# Output: [1, 5, 6]
# Explanation: The smallest missing positive numbers are 1, 5 and 6.
# Example 3:

# Input: [-2, -3, 4], k=2
# Output: [1, 2]
# Explanation: The smallest missing positive numbers are 1 and 2.


def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def getKthMissing(array, k):
    i = 0
    n = len(array)
    miss = []
    while i < n:
        j = array[i] - 1
        if array[i] < n and array[i] > 0 and array[j] != array[i]:
            swap(i, j, array)
        else:
            i += 1
    
    for i in range(len(array) + k):
        if i < len(array): 
            if i + 1 != array[i]:
                if (i + 1) not in array:
                    miss.append(i + 1)
        else:
            if (i + 1) not in array:
                miss.append(i + 1)


        if len(miss) == k:
            return miss

    return miss

if __name__ == '__main__':
    array1 = [3, -1, 4, 5, 5]
    array2 = [2, 3, 4]
    array3 = [-2, -3, 4]

    out1 = [1, 2, 6]
    out2 = [1, 5, 6]
    out3 = [1,2]

    r1 = getKthMissing(array1, 3)
    r2 = getKthMissing(array2, 3)
    r3 = getKthMissing(array3, 2)

    print(r1)
    print(r2)
    print(r3)
    assert out1 == r1
    assert out2 == r2
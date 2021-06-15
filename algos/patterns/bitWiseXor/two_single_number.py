# In a non-empty array of numbers, every number appears exactly twice except two numbers that appear only once. Find the two numbers that appear only once.

# Example 1:

# Input: [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
# Output: [4, 6]
# Example 2:

# Input: [2, 1, 3, 2]
# Output: [1, 3]

def getTheDoubleNumber(arr):
    '''
    Time: O(n)
    Space: O(1)
    '''

    # 1. First xor all numbers, the result will have the XOR of the two different numbers.
    n1xn2 = 0
    for i in arr:
        n1xn2 ^= i
    # 2. Next set the right most bit which is 1 and divide the numbers into two groups.
    rightMostBit = 1
    while (rightMostBit & n1xn2) == 0:
        rightMostBit = rightMostBit << 1
    num1, num2 = 0, 0

    for num in arr:
        if (num & rightMostBit) != 0: # the bit is set
            num1 ^= num
        else: # the bit is not set
            num2 ^= num

    return [num2, num1]


if __name__ == '__main__':

    arr1 = [1, 4, 2, 1, 3, 5, 6, 2, 3, 5]
    arr2 = [2, 1, 3, 2]

    r1 = getTheDoubleNumber(arr1)
    r2 = getTheDoubleNumber(arr2)

    print(r1, r2)
    assert r1 == [4, 6]
    assert r2 == [1, 3]


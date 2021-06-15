# In a non-empty array of integers, every number appears twice except for one, find that single number.

# Example 1:

# Input: 1, 4, 2, 1, 3, 2, 3
# Output: 4
# Example 2:

# Input: 7, 9, 7
# Output: 9

def getTheNumber(arr):
    '''
    Time: O(n)
    Space: O(1)
    '''
    x = 0
    for i in arr:
        x ^= i
    return x

if __name__ == '__main__':

    arr1 = [1, 4, 2, 1, 3, 2, 3]
    arr2 = [7, 9, 7]
    arr3 = [1]

    r1 = getTheNumber(arr1)
    r2 = getTheNumber(arr2)
    r3 = getTheNumber(arr3)
    print(r1, r2, r3)
    assert r1 == 4
    assert r2 == 9
    assert r3 == 1

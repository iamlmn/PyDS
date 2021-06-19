# Given an array of numbers sorted in ascending order, find the range of a given number ‘key’. The range of the ‘key’ will be the first and last position of the ‘key’ in the array.

# Write a function to return the range of the ‘key’. If the ‘key’ is not present return [-1, -1].

# Example 1:

# Input: [4, 6, 6, 6, 9], key = 6
# Output: [1, 3]
# Example 2:

# Input: [1, 3, 8, 10, 15], key = 10
# Output: [3, 3]
# Example 3:

# Input: [1, 3, 8, 10, 15], key = 12
# Output: [-1, -1]



def getNumberRange():
    ret = [-1, -1]
    ret[0] = doBinarySearch(arr, key, False)

    if ret[0] != -1:
        ret[1] = doBinarySearch(arr, key, True)

    return ret

def doBinarySearch(arr, key, FindMaxFlag, left=0):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right)//2
        if key > arr[left]:
            left = mid + 1 
        elif key < arr[right]:
            right = mid - 1

        else:
            key = mid
            if findMax:
                left = mid + 1

            else:
                right = mid - 1
        return key



if __name__ == '__main__':
    arr1 = []
    key1 
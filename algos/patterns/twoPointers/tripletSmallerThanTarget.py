# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def countSmallerThanTarget(array, target):
    triplets = []

    array.sort()

    for i in range(len(array) - 2):
        search_pair(array, target - array[i], i, i+ 1, triplets)

    return len(triplets)

def search_pair(array, targetSum, i, left, triplets):
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]
        if currentSum < targetSum:
            r = right
            while r > left:
                triplets.append([array[i] , array[left], array[r]])
                r -= 1
            left += 1
        else:
            right -= 1



if __name__ == '__main__':
    nums1 = [-1, 0, 2, 3]
    target1 = 3

    x1 = countSmallerThanTarget(nums1, target1)
    print(x1)
    assert x1 == 2


    x2 = countSmallerThanTarget([-1, 4, 2, 1, 3], 5)
    print(x2)
    assert x2 == 4



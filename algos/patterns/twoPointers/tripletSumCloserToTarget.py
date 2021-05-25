# Given an array of unsorted numbers and a target number, find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. If there are more than one such triplet, return the sum of the triplet with the smallest sum.

# Example 1:

# Input: [-2, 0, 1, 2], target=2
# Output: 1
# Explanation: The triplet [-2, 1, 2] has the closest sum to the target.
# Example 2:

# Input: [-3, -1, 1, 2], target=1
# Output: 0
# Explanation: The triplet [-3, 1, 2] has the closest sum to the target.
# Example 3:

# Input: [1, 0, 1, 1], target=100
# Output: 3
# Explanation: The triplet [1, 1, 1] has the closest sum to the target.
import math
global tripletSum
global nearestTripletSum
def findClosestTripletSum(array, target):
    array.sort()
    global tripletSum
    global nearestTripletSum
    nearestTripletSum = math.inf

    tripletSum = math.inf
    
    for i in range(len(array)):
        search_pair(array, target -  array[i]  , i + 1, target)
    return tripletSum


def search_pair(array, targetSum, left, target):
    right = len(array) - 1
    global tripletSum
    global nearestTripletSum
    while left < right:
        currentSum = array[left] + array[right] 
        diff = currentSum - targetSum
        # print(min(abs(currentSum - targetSum), abs(nearestTripletSum)))
        if abs(diff) < nearestTripletSum:
            # print(currentSum - targetSum , nearestTripletSum, "suo")
            nearestTripletSum = abs(diff)

            tripletSum = currentSum - targetSum + target

        elif abs(diff) == nearestTripletSum:
            tripletSum = min(currentSum - targetSum + target, tripletSum)
            
        if currentSum == targetSum:
            nearestTripletSum = 0
        elif currentSum < targetSum:
            left += 1
        else:
            right -= 1

    # return tripletSum
        

if __name__ == '__main__':

    nums1 = [-2, 0, 1, 2]
    target1 = 2

    x1 = findClosestTripletSum(nums1, target1)
    print(x1)
    assert x1 == 1
    nums2 = [-3, -1, 1, 2]
    target2 = 1
    x2 = findClosestTripletSum(nums2, target2)
    print(x2)
    assert x2 == 0
    nums3 = [1, 0, 1, 1]
    target3 = 100
    x3 = findClosestTripletSum(nums3, target3)
    print(x3)
    assert x3 == 3

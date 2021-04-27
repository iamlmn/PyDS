# Given an array of unsorted numbers and a target number, 
# find a triplet in the array whose sum is as close to the target number as possible, return the sum of the triplet. 
# If there are more than one such triplet, return the sum of the triplet with the smallest sum.

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

def closestTarget(array, target):
    array.sort()
    smallestDiff = math.inf
    for i in range(len(array) - 2):
        left = i + 1    
        right = len(array) - 1

        while left < right:
            currentSum = array[i] + array[left] + array[right]
            targetDiff = target - currentSum
            if target == currentSum:
                return currentSum
            
            if abs(smallestDiff) > abs(targetDiff):
                smallestDiff = targetDiff

            if targetDiff > 0:
                left += 1
            else:
                right -= 1

    return target- smallestDiff

if __name__ == '__main__':
    print(closestTarget([-2, 0, 1, 2], 2))
    
    print(closestTarget([-3, -1, 1, 2], 1))
    print(closestTarget([1, 0, 1, 1], 100))
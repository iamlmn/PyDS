# Minimum Window Sort (medium) #
# Given an array, find the length of the smallest subarray in it which when sorted will sort the whole array.

# Example 1:

# Input: [1, 2, 5, 3, 7, 10, 9, 12]
# Output: 5
# Explanation: We need to sort only the subarray [5, 3, 7, 10, 9] to make the whole array sorted
# Example 2:

# Input: [1, 3, 2, 0, -1, 7, 10]
# Output: 5
# Explanation: We need to sort only the subarray [1, 3, 2, 0, -1] to make the whole array sorted
# Example 3:

# Input: [1, 2, 3]
# Output: 0
# Explanation: The array is already sorted
# Example 4:

# Input: [3, 2, 1]
# Output: 3
# Explanation: The whole array needs to be sorted.

import math

def checkSorted(nums): 
    low = 0
    high = len(nums) - 1

    for i in range(1, len(nums) - 1):
        if nums[i] > nums[i - 1]:
            low += 1
        else:
            break

    for i in range(len(nums) - 1, 0, -1):
        if nums[i] > nums[i - 1]:
            high -= 1
        else:
            # print("Breaking hifgh")
            break

    if high == 0:
        return 0

    if low == 0:
        return len(nums)

    minSub = math.inf
    maxSub = -math.inf
    for i in range(low, high + 1):
        minSub = min(minSub, nums[i])
        maxSub = max(maxSub, nums[i])

    for i in range(0, low):
        if nums[i] > minSub:
            low = i
            break

    for i in range(high, len(nums)):
        if nums[i] < maxSub:
            high = i
            
    
    # return low, high, minSub, maxSub
    return abs(high - low + 1) 



if __name__ == '__main__':
    list1 = [1, 2, 5, 3, 7, 10, 9, 12]
    list2 = [1, 3, 2, 0, -1, 7, 10]
    list3 = [1, 2, 3]
    list4 = [3, 2, 1]
    print(checkSorted(list1))
    print(checkSorted(list2))
    print(checkSorted(list3))
    print(checkSorted(list4))
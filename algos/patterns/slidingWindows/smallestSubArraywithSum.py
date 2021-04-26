# Given an array of positive numbers and a positive number ‘S’, find the length of the smallest contiguous subarray whose sum is greater than or equal to ‘S’. Return 0, if no such subarray exists.

# Example 1:

# Input: [2, 1, 5, 2, 3, 2], S=7 
# Output: 2
# Explanation: The smallest subarray with a sum great than or equal to '7' is [5, 2].
# Example 2:

# Input: [2, 1, 5, 2, 8], S=7 
# Output: 1
# Explanation: The smallest subarray with a sum greater than or equal to '7' is [8].
# Example 3:

# Input: [3, 4, 1, 1, 6], S=8 
# Output: 3
# Explanation: Smallest subarrays with a sum greater than or equal to '8' are [3, 4, 1] or [1, 1, 6].


def smallestSubArray(array, s):
    '''

    Time complexity : O(N)
    space : O(N)

    '''


    start = 0
    minWindow = len(array) + 1
    currentSum = 0
    for i in range(len(array)):
        currentSum += array[i]

        while currentSum >= s:

            minWindow = min(minWindow, i - start + 1)
            currentSum -= array[start]
            start += 1

    
    if minWindow > len(array):
        return 0

    return minWindow


    

    
    if minWindow is None:
        return 0

    return minWindow



if __name__ =='__main__':
    print(f"smallest subarray {smallestSubArray([2, 1, 5, 2, 3, 2], 7)}")
    print(f"smallest subarray {smallestSubArray([2, 1, 5, 2, 8], 7)}")
    print(f"smallest subarray {smallestSubArray([3, 4, 1, 1, 6], 8)}")

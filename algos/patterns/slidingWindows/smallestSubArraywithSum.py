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
    cs = 0
    import math
    minWindow = math.inf

    for i in range(len(array)):
        cs += array[i]

        while cs >= s:  # this cant be if since we might have to remove multiple number if the last numbwer added is very large.
            minWindow = min(minWindow, i - start + 1)
            cs -= array[start]
            start += 1

    return minWindow if minWindow != math.inf else 0



if __name__ =='__main__':
    print(f"smallest subarray {smallestSubArray([2, 1, 5, 2, 3, 2], 7)}")
    print(f"smallest subarray {smallestSubArray([2, 1, 5, 2, 8], 7)}")
    print(f"smallest subarray {smallestSubArray([3, 4, 1, 1, 6], 8)}")

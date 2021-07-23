# Given an array of positive numbers and a positive number ‘k’, find the maximum sum of any contiguous subarray of size ‘k’.

# Example 1:

# Input: [2, 1, 5, 1, 3, 2], k=3 
# Output: 9
# Explanation: Subarray with maximum sum is [5, 1, 3].
# Example 2:

# Input: [2, 3, 4, 1, 5], k=2 
# Output: 7
# Explanation: Subarray with maximum sum is [3, 4].




def maxSubarrayOfSizeK(array, k):
    '''
    Time complexity : O(N)
    Space Complexity : O(1)
    '''
    start = 0
    currentSum = 0
    maxSum = 0
    
    for end in range(len(array)):
        if end < k:
            currentSum += array[end]

        if end >= k:
            currentSum += array[end]
            currentSum -= array[start]
            start += 1
            maxSum = max(maxSum, currentSum)

    return maxSum
        
if __name__ == '__main__':
    array = [2, 1, 5, 1, 3, 2]
    array2 = [2, 3, 4, 1, 5]

    print(f"{maxSubarrayOfSizeK(array, 3)}")
    print(f"{maxSubarrayOfSizeK(array2, 2)}")
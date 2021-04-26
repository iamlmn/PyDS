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
    currentSum = 0
    maxSum = array[0]
    start = 0

    if len(array) < k:
        return 0
    for i in range(len(array)):
        currentSum += array[i]
     

        if i > k -1:
            currentSum -= array[start]
            start += 1
            maxSum = max(currentSum,maxSum)


    return maxSum
if __name__ == '__main__':
    array = [2, 1, 5, 1, 3, 2]
    array2 = [2, 3, 4, 1, 5]

    print(f"{maxSubarrayOfSizeK(array, 3)}")
    print(f"{maxSubarrayOfSizeK(array2, 2)}")
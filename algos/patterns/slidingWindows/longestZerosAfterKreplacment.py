# Given an array containing 0s and 1s, if you are allowed to replace no more than ‘k’ 0s with 1s, find the length of the longest contiguous subarray having all 1s.

# Example 1:

# Input: Array=[0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1], k=2
# Output: 6
# Explanation: Replace the '0' at index 5 and 8 to have the longest contiguous subarray of 1s having length 6.
# Example 2:

# Input: Array=[0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1], k=3
# Output: 9
# Explanation: Replace the '0' at index 6, 9, and 10 to have the longest contiguous subarray of 1s having length 9.


def longestSubStringAfterReplacement(listInput, k):
    '''
    time complexity : O(n)
    space : O(1)
    '''
    start = 0
    end = 0
    maxLength = 0
    nOnes = 0
    for i in range(len(listInput)):
        if listInput[i] == 1:
            nOnes += 1
        if (i - start + 1 - nOnes > k):
            if listInput[start] == 1:
                nOnes -= 1
            start += 1
        maxLength = max(maxLength, i - start + 1)

    return maxLength


    
if __name__ == '__main__':
    list1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    list2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    print(f"longestSubStringAfterReplacement{longestSubStringAfterReplacement(list1, 2)}")
    print(f"longestSubStringAfterReplacement{longestSubStringAfterReplacement(list2, 3)}")
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
    maxLength,numOnes, start = 0, 0, 0
    
    
    for i in range(len(listInput)):
        if listInput[i] == 1:
            numOnes += 1
        if (i - start + 1 - numOnes) > k:
            if listInput[start] == 1:
                numOnes -= 1
            start += 1

        maxLength = max(maxLength, i - start + 1)
    return maxLength

def longestSubStringAfterReplacement_2(listInput, k):
    maxLength,numZeros, start = 0, 0, 0

    for i in range(len(listInput)):
        if listInput[i] == 0:
            numZeros += 1

        if numZeros > k:
            if listInput[start] == 0:
                numZeros -= 1
            start += 1

        maxLength = max(maxLength, i - start + 1)
    return maxLength
    
if __name__ == '__main__':
    list1 = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
    list2 = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
    longestSubStringAfterReplacement = longestSubStringAfterReplacement_2
    print(f"longestSubStringAfterReplacement{longestSubStringAfterReplacement(list1, 2)}")
    print(f"longestSubStringAfterReplacement{longestSubStringAfterReplacement(list2, 3)}")
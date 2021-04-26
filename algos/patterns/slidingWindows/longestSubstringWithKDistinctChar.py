# Longest Substring with K Distinct Characters

# Given a string, find the length of the longest substring in it with no more than K distinct characters.

# Example 1:

# Input: String="araaci", K=2
# Output: 4
# Explanation: The longest substring with no more than '2' distinct characters is "araa".


# Input: String="araaci", K=1
# Output: 2
# Explanation: The longest substring with no more than '1' distinct characters is "aa".


def findLongSubString(stringArray, k):
    '''
    Time complexity : O(N),
    Space: O(k) where we store K + 1 characters.
    '''

    maxSubstringLength = 0
    start = 0
    charFrequency = {}
    for i in range(len(stringArray)):
        
        if stringArray[i] not in charFrequency:
            charFrequency[stringArray[i]] = 0
        charFrequency[stringArray[i]] += 1


        while len(charFrequency) > k:
            charFrequency[stringArray[start]] -= 1
            if charFrequency[stringArray[start]] == 0:
                del charFrequency[stringArray[start]]
            start += 1

        maxSubstringLength = max(maxSubstringLength, i - start + 1)

    return maxSubstringLength

if __name__ =='__main__':
    string1 = "araaci"
    string2 = "cbbebi"
    print(f"maxSubstringLength {findLongSubString(string1, 2)}")
    print(f"maxSubstringLength {findLongSubString(string1, 1)}")
    print(f"maxSubstringLength {findLongSubString(string2, 3)}")
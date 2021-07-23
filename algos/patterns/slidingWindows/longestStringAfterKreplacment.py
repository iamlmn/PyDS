# Given a string with lowercase letters only, if you are allowed to replace no more than ‘k’ letters with any letter, find the length of the longest substring having the same letters after replacement.

# Example 1:

# Input: String="aabccbb", k=2
# Output: 5
# Explanation: Replace the two 'c' with 'b' to have a longest repeating substring "bbbbb".
# Example 2:

# Input: String="abbcb", k=1
# Output: 4
# Explanation: Replace the 'c' with 'b' to have a longest repeating substring "bbbb".
# Example 3:

# Input: String="abccde", k=1
# Output: 3
# Explanation: Replace the 'b' or 'd' with 'c' to have the longest repeating substring "ccc".



def longestSubStringAfterReplacement(stringInput, k):
    start = 0
    end = 0
    charFrequency = {}
    outputString = ''
    maxLength = 0
    maxRepeatLetterCount = 0
    for i in range(0, len(stringInput)):
        cChar = stringInput[i]
        if cChar not in charFrequency:
            charFrequency[cChar]=  0
        charFrequency[cChar] += 1

        maxRepeatLetterCount = max(maxRepeatLetterCount,  charFrequency[cChar])

        if (i - start + 1 - maxRepeatLetterCount) > k:
            rChar = stringInput[start]
            charFrequency[rChar] -= 1
            start += 1
        maxLength = max(maxLength, i - start + 1)
    
    return maxLength

if __name__ == '__main__':
    string1 = 'aabccbb'
    string2 = 'abbcb'
    string3  = 'abccde'
    print(f" aabccbb :  {longestSubStringAfterReplacement(string1, 2)}")
    print(f"abbcb : {longestSubStringAfterReplacement(string2, 1)}")
    print(f" abccde:  {longestSubStringAfterReplacement(string3, 1)}")
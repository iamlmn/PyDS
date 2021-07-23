# Given a string, find the length of the longest substring which has no repeating characters.

# Example 1:

# Input: String="aabccbb"
# Output: 3
# Explanation: The longest substring without any repeating characters is "abc".
# Example 2:

# Input: String="abbbb"
# Output: 2
# Explanation: The longest substring without any repeating characters is "ab".
# Example 3:

# Input: String="abccde"
# Output: 3
# Explanation: Longest substrings without any repeating characters are "abc" & "cde".



def noRepeatString(stringInput):
    start = 0
    outputString = ''
    charFrequency = {}
    maxSubstringLength = 0
    for i in range(len(stringInput)):
        cChar =  stringInput[i]
        if cChar in charFrequency:
            start = max(start, charFrequency[cChar] + 1)
        charFrequency[cChar] = i
        maxSubstringLength = max(maxSubstringLength, i - start + 1)

        
    return maxSubstringLength


if __name__ == '__main__':
    stringInput = 'aabccbb'
    string2 = 'abbbb'
    string3 = 'abccde'
    print(f"{noRepeatString(stringInput)}")
    print(f"{noRepeatString(string2)}")
    print(f"{noRepeatString(string3)}")
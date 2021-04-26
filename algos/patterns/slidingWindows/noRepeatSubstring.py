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
    end = 0
    outputString = ''
    charFrequency = {}

    for i in range(len(stringInput)):
        if stringInput[i] not in charFrequency:
            charFrequency[stringInput[i]] = 0
        charFrequency[stringInput[i]] += 1

        while sum(charFrequency.values()) > len(charFrequency):
            charFrequency[stringInput[start]] -= 1
            if charFrequency[stringInput[start]] == 0:
                del charFrequency[stringInput[start]]
                if len(outputString) < len(stringInput[start: i]):
                    outputString = stringInput[start: i]
            start += 1
    return len(outputString)


if __name__ == '__main__':
    stringInput = 'aabccbb'
    string2 = 'abbbb'
    string3 = 'abccde'
    print(f"{noRepeatString(stringInput)}")
    print(f"{noRepeatString(string2)}")
    print(f"{noRepeatString(string3)}")
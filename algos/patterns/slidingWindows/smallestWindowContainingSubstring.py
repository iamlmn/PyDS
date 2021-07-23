# Smallest Window containing Substring (hard) #
# Given a string and a pattern, find the smallest substring in the given string which has all the characters of the given pattern.

# Example 1:

# Input: String="aabdec", Pattern="abc"
# Output: "abdec"
# Explanation: The smallest substring having all characters of the pattern is "abdec"
# Example 2:

# Input: String="abdabca", Pattern="abc"
# Output: "abc"
# Explanation: The smallest substring having all characters of the pattern is "abc".
# Example 3:

# Input: String="adcad", Pattern="abc"
# Output: ""
# Explanation: No substring in the given string has all characters of the pattern.


def findSmallestWindow(stringInput, subString):
    '''
    create a counter of chars in substring and store it as hash map.
    keep increasing window end untill everythhing becomes zero and start shrinking from left untill everything in the counter/hash has values as 0.
    '''
    start = 0
    charFrequency = {}
    minLength = len(stringInput)
    matched = 0
    outputString = ""

    for i in range(len(subString)):
        if subString[i] not in charFrequency:
            charFrequency[subString[i]] = 0
        charFrequency[subString[i]] += 1

    for i in range(len(stringInput)):
        cChar = stringInput[i]
        if cChar in charFrequency:
            charFrequency[cChar] -= 1
            
            if charFrequency[cChar] == 0:
                matched += 1

        while matched == len(charFrequency):
            # found all chars, now try shrinking the window.
            rChar = stringInput[start]
            start += 1
            if rChar in charFrequency:
                if charFrequency[rChar] == 0:
                    matched -= 1
                charFrequency[rChar] += 1
        
            minLength = min(minLength, i - start + 1)
            outputString = stringInput[start - 1: i + 1]
            
            
    return outputString


if __name__ == '__main__':
    string1 = 'aabdec'
    substring = 'abc'
    string2 = 'abdabca'
    string3 = 'adcad'
    print(f"aabdec, abc : {findSmallestWindow(string1, substring)}")
    print(f"abdabca, abc : {findSmallestWindow(string2, substring)}")
    print(f"adcad, abc : {findSmallestWindow(string3, substring)}")

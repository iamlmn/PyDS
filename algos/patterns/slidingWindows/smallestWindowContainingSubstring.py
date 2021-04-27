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
    start = 0
    outputString = ''
    charFrequency = {}

    for i in range(len(subString)):
        if subString[i] not in charFrequency:
            charFrequency[subString[i]] = 0
        charFrequency[subString[i]] += 1
    # print(charFrequency)
    i = 0
    flag = 0
    for i in range(len(stringInput)): # and 
        if stringInput[i] in charFrequency:
            charFrequency[stringInput[i]] -= 1
            if charFrequency[stringInput[i]] == 0:
                flag += 1

        while flag == len(charFrequency):
            print(stringInput[start: i + 1])
            if len(outputString) > len(stringInput[start: i + 1]) or outputString == '':
                outputString = stringInput[start: i + 1]

            if stringInput[start] in charFrequency:
                charFrequency[stringInput[start]] += 1
                if charFrequency[stringInput[start]] > 0:
                    flag -= 1
            start += 1

    return outputString


if __name__ == '__main__':
    string1 = 'aabdec'
    substring = 'abc'
    string2 = 'abdabca'
    string3 = 'adcad'
    print(f"Sup : {findSmallestWindow(string1, substring)}")
    print(f"Sup : {findSmallestWindow(string2, substring)}")
    print(f"Sup : {findSmallestWindow(string3, substring)}")

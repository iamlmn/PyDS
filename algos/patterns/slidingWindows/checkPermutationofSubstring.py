# Given a string and a pattern, find out if the string contains any permutation of the pattern.

# Permutation is defined as the re-arranging of the characters of the string. For example, “abc” has the following six permutations:

# abc
# acb
# bac
# bca
# cab
# cba
# If a string has ‘n’ distinct characters it will have n!n! permutations.

# Example 1:

# Input: String="oidbcaf", Pattern="abc"
# Output: true
# Explanation: The string contains "bca" which is a permutation of the given pattern.
# Example 2:

# Input: String="odicf", Pattern="dc"
# Output: false
# Explanation: No permutation of the pattern is present in the given string as a substring.
# Example 3:

# Input: String="bcdxabcdy", Pattern="bcdyabcdx"
# Output: true
# Explanation: Both the string and the pattern are a permutation of each other.
# Example 4:

# Input: String="aaacb", Pattern="abc"
# Output: true
# Explanation: The string contains "acb" which is a permutation of the given pattern.



def checkPattern(stringInput, patternInput):
    start = 0
    charFrequency = {}
    for i in range(len(patternInput)):
        if patternInput[i] not in charFrequency:
            charFrequency[patternInput[i]] = 0
        charFrequency[patternInput[i]] += 1

    print(charFrequency)
    for i in range(len(stringInput)):
        if stringInput[i] in charFrequency:
            charFrequency[stringInput[i]] -= 1
        if i >= len(patternInput) - 1:
            if sum(charFrequency.values()) == 0:
                return True, start, i
            if stringInput[start] in charFrequency:
                charFrequency[stringInput[start]] += 1
            start += 1
    return False

        

if __name__ == '__main__':

    string1 = 'oidbcaf'
    pattern1 ='abc'

    print(f"{string1} - pattern {pattern1} : {checkPattern(string1, pattern1)}")    

    string2 = 'odicf'
    pattern2 ='dc'
    print(f"{string2} - pattern {pattern2} : {checkPattern(string2, pattern2)}")


    string3 = 'bcdxabcdy'
    pattern3 ='bcdyabcdx'
    print(f"{string3} - pattern {pattern3} : {checkPattern(string3, pattern3)}")

    
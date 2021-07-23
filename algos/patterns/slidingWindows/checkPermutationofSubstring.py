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
    '''
    TC: O(N + M)
    Space: O(M)
    1. Caluclate patterFrequency
    2. Got though string and decrease frequency. if fre = 0, have a counter. if it reaches num of distinct chars in pattern string it means every thing is present.
    3. If window len goes beyond patternwindows, start ++ , if its present in windwo, make sure to decrement matched counter and increased counter value in frequency.
    '''
    start, matched, windowLength, patternFrequency = 0, 0, len(patternInput), {}
    # set pattern frequency.
    for i in range(windowLength):
        if patternInput[i] not in patternFrequency:
            patternFrequency[patternInput[i]] = 0
        patternFrequency[patternInput[i]] += 1

    for i in range(len(stringInput)):
        cChar = stringInput[i]
        if cChar in patternFrequency:
            patternFrequency[cChar] -= 1
            if patternFrequency[cChar] == 0:
                matched += 1

        if matched == len(patternFrequency):
            return True
        
        if i >= windowLength - 1:
            rChar = stringInput[start]
            start += 1
            if rChar in patternFrequency:
                if patternFrequency[rChar] == 0:
                    matched -= 1
                patternFrequency[rChar] += 1
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

    
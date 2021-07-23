# Given a string and a pattern, find all anagrams of the pattern in the given string.

# Anagram is actually a Permutation of a string. For example, “abc” has the following six anagrams:

# abc
# acb
# bac
# bca
# cab
# cba
# Write a function to return a list of starting indices of the anagrams of the pattern in the given string.

# Example 1:

# Input: String="ppqp", Pattern="pq"
# Output: [1, 2]
# Explanation: The two anagrams of the pattern in the given string are "pq" and "qp".
# Example 2:

# Input: String="abbcabc", Pattern="abc"
# Output: [2, 3, 4]
# Explanation: The three anagrams of the pattern in the given string are "bca", "cab", and "abc".


def checkAnagram(stringInput, patternInput):
    '''
    TC : O(N + M)
    SC : O(M)

    1. Store patternInput counter to a hashmap.
    2. Loop through string input with window len = len(patterinput) and keep decrementing counter of chars if it is present in counter hashmap.
    3. if everything is 0 store start to resultant array and Continue.
    '''
    start, matched, startIndices, patternFrequency = 0, 0, [], {}
    windowLength = len(patternInput)
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
            startIndices.append(start)
        
        if i >= windowLength - 1:
            rChar = stringInput[start]
            start += 1
            if rChar in patternFrequency:
                if patternFrequency[rChar] == 0:
                    matched -= 1
                patternFrequency[rChar] += 1

    return startIndices


if __name__ == '__main__':
    string1 = 'ppqp'
    pattern1 = 'pq'
    string2 = 'abbcabc'
    pattern2 = 'abc'
    print(f"{checkAnagram(string1, pattern1)}")
    print(f"{checkAnagram(string2, pattern2)}")



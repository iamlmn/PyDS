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
    start = 0
    startIndices = []
    patternFrequency = {}

    for i in patternInput:
        if i not in patternFrequency:
            patternFrequency[i] = 0
        patternFrequency[i] += 1
    backUpFrequency = patternFrequency
    
    for i in range(len(stringInput)):
        
        if stringInput[i] in patternFrequency:
            patternFrequency[stringInput[i]] -= 1
        if i >= len(patternInput) - 1:
            if list(set(patternFrequency.values())) == [0]:
                startIndices.append(start)

            if stringInput[start] in patternFrequency:
                patternFrequency[stringInput[start]] += 1
            start += 1

    return startIndices



if __name__ == '__main__':
    string1 = 'ppqp'
    pattern1 = 'pq'
    string2 = 'abbcabc'
    pattern2 = 'abc'
    print(f"{checkAnagram(string1, pattern1)}")
    print(f"{checkAnagram(string2, pattern2)}")



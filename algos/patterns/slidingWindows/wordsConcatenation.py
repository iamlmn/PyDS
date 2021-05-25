# Words Concatenation (hard) #
# Given a string and a list of words, find all the starting indices of substrings in the 
# given string that are a concatenation of all the given words exactly once without any 
# overlapping of words. It is given that all words are of the same length.

# Example 1:

# Input: String="catfoxcat", Words=["cat", "fox"]
# Output: [0, 3]
# Explanation: The two substring containing both the words are "catfox" & "foxcat".
# Example 2:

# Input: String="catcatfoxfox", Words=["cat", "fox"]
# Output: [3]
# Explanation: The only substring containing both the words is "catfox".


def concatenateWords(stringInput, words):
    
    outputIndices = []
    wordFrequency = {}
    wordsCount = len(words)
    wordLength = len(words[0])
    totalLen = wordsCount * wordLength

    for i in words:
        if i not in wordFrequency:
            wordFrequency[i] = 0
        wordFrequency[i] += 1


    for i in range(0, len(stringInput) - totalLen + 1):
        wordSeen = {}
        for j in range(wordsCount):
            word = stringInput[ i + j*wordLength:i + j*wordLength + wordLength]
        
            if word not in wordFrequency:
                break

            if word not in wordSeen:
                wordSeen[word] = 0
            wordSeen[word] += 1

            if wordSeen[word] > wordFrequency[word]:
                break
            
            if j + 1== wordsCount :
                outputIndices.append(i)

    return outputIndices


if __name__ == '__main__':
    string1 = 'catfoxcat'
    words = ['cat', 'fox']
    string2 = 'catcatfoxfox'

    print(f" {concatenateWords(string1, words)}")
    print(f" {concatenateWords(string2, words)}")
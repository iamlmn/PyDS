'''
Word Search
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, 
where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true

Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

[["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
"ABCESEEEFS"
'''

def validate(mat, i, j, words, k):
    if i < 0 or j < 0 or i >= len(mat) or j >= len(mat[0]) or mat[i][j] != words[k]:
        return False
    return True

def word_search(mat, i, j, words, k):
    if k >= len(words):
        return True
    if not validate(mat, i, j, words, k):
        return False
    visit = mat[i][j]
    mat[i][j] = '#'
    if visit == words[k]:
        res = word_search(mat, i + 1, j, words, k + 1) or word_search(mat, i - 1, j, words, k + 1) or word_search(mat, i, j + 1, words, k + 1) or word_search(mat, i , j - 1, words, k + 1)
    mat[i][j]  = visit
    return res

if __name__ == '__main__':
    word1 = ""
    word2 = "ABCCED"
    word3 = "SEE"
    word4 = "ABCB" 
    word5 = "ABCESCFS"
    mat = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word_list = [word1, word2, word3, word4, word5]
    outputs = [True, True, True, False, True]
    for word, out in zip(word_list, outputs):
        flag = False
        k = 0
        for i in range(len(mat)):
            if flag:
                break
            for j in range(len(mat[0])):
                if k == len(word):
                    flag = True
                    break
                if mat[i][j] == word[k]:
                    if word_search(mat, i, j, word, k):
                        flag = True
                        break
        assert flag == out
        print(f"Search results of {word} in {mat}  :", flag)
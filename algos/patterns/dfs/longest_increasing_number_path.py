'''
Longest increasing numerical path.

Return the longest increasing number path
11 9 0 4 5 8
1 0 2 4 16 4
0 4 3 18 17 8
9 3 4 19 100 1
1 8 2 399 102 3
Op: 10 [ 0, 2, 4, 16, 17, 18, 19 ,100, 102, 399]

Example 2:

1 2
4 3
op : 4 [1,2,3,4]
'''

def validate(mat, i, j, parent, dp):
    if i < 0 or j < 0 or j >= len(mat[0]) or i >= len(mat) or mat[i][j] == '#' or mat[i][j] <= parent:
        return False
    return True

def dfs(mat, i, j, parent, dp):
    '''
    Ask my neighbors whats their max number of inc paths from them and choose the best/max direction from their results.
    '''
    if not validate(mat, i, j, parent, dp):
        return 0
    if dp[i][j] != -1:
        return dp[i][j] + 1
    temp = mat[i][j]
    mat[i][j] = '#'  # setting to visited
    dp[i][j] = max(dfs(mat, i + 1, j, temp, dp),dfs(mat, i - 1, j, temp, dp), dfs(mat, i , j + 1, temp, dp), dfs(mat, i, j - 1, temp, dp))
    mat[i][j] = temp # change back to original value while backtracking.
    return dp[i][j] + 1

if __name__ == '__main__':
    mat0 = [[1]]
    mat1 = [[1,2], [3, 4]] # 3
    mat2 = [[1,2], [4, 3]] # 4
    mat3 = [[9,9,4],[6,6,8],[2,1,1]] # 4
    mat4 = [[3,4,5],[3,2,6],[2,2,1]] # 4
    mat5 = [[11, 9 ,0 ,4,5, 8], [1, 0, 2 ,4 ,16, 4], [0, 4, 3, 18, 17, 8], [9 , 3, 4, 19, 100 , 1], [1 , 8, 2, 399, 102, 3] ] #10
    mat6 = [[2,1], [3, 4]]
    inputs = [[[]], mat0, mat1, mat2, mat3, mat4, mat5]
    outputs = [0, 1, 3, 4, 4, 4, 10, 4]
    for l, mat in enumerate(inputs):
        dp = [[-1 for i in range(len(mat) + 1)] for j in range(len(mat[0]))] # store max paths from each point. 
        res, o = [], 0
        visited = set()
        for i in range(len(mat)):
            for j in range(len(mat[0])):

                if (i,j) not in visited:
                    res.append(dfs(mat, i, j, -1, dp))
        print(res)
        if res:
            o = max(res)

        assert o == outputs[l]
        print("Max increasing path in ", mat, o)
    
'''
How can we optimize? In forr loop we will be doing some redundant work of calculating max path.
if we could store it avoid doing it redundant work, time complexity will improve.
'''

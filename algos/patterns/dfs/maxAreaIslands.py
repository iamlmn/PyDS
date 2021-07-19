'''
Calculate the area of an island
'''
def validate(matrix, i, j,visited):
    if j < 0 or i < 0 or i >= len(matrix) or j >= len(matrix[0]) or (i,j) in visited or matrix[i][j] != 1:
        return False
    return True

def explore_islands_using_dfs(mat, i, j, visited, res=[]):
    if not validate(mat, i,j, visited):
        return 0
    
    visited.add((i,j))
    # print(i,j, visited)
    num_ones = explore_islands_using_dfs(mat, i + 1, j, visited) + explore_islands_using_dfs(mat, i - 1, j, visited) + explore_islands_using_dfs(mat, i, j + 1, visited) + explore_islands_using_dfs(mat, i, j - 1, visited)
    #print(i,j, num_ones)
    if mat[i][j] == 1:
        return num_ones + 1
    return num_ones

if __name__ == '__main__':
    visited = set()
    res = []
    mat = [[0, 0, 1], [0, 0, 0], [1,1,1]]
    for i in range(len(mat)):
        for j in range(len(mat[0])):

            if (i,j) in visited:
                continue
            # visited.add((i,j))

            if mat[i][j] == 1:
                res.append(explore_islands_using_dfs(mat, i, j, visited))

    print("Max area of island present is ", mat, max(res))
'''
Calculate the sum of all positive numbers from a given 
matrix using backsolving / with out using global vairables
'''
def validate(matrix, i, j,visited):
    if j < 0 or i < 0 or i >= len(matrix) or j >= len(matrix[0]) or (i,j) in visited:
        return False
    return True

def backsolve_dfs(mat, idx, idy, visited):
    '''
    Ask my next number how many positives 
    number he sees and return their sum to parent.
    '''
    if not validate(mat, idx, idy, visited):
        return 0
    visited.add((idx,idy))
    my_sum = backsolve_dfs(l, idx + 1, idy, visited)  + backsolve_dfs(l, idx  -1, idy, visited) + backsolve_dfs(l, idx, idy + 1, visited) + backsolve_dfs(l, idx, idy - 1, visited)
    if mat[idx][idy] > 0:
        return my_sum + mat[idx][idy]
    return my_sum

if __name__ == '__main__':
    visited= set()
    l = [[1,2, 0, 17], [-4, 3, 6, 0], [0, 0, 7, 1], [-14, -1, 3, 100]]
    print(backsolve_dfs(l, 0,0, visited))
    ts = 0
    for i in range(len(l)):
        for j in range(len(l[0])):
            if l[i][j] > 0:
                ts += l[i][j]
    print(ts)
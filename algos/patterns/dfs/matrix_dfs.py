
def validate(matrix, i, j,visited):
    if j < 0 or i < 0 or i >= len(matrix) or j >= len(matrix[0]) or (i,j) in visited:
        return False
    return True

def dfs(l, idx,idy, visited, num):
    global res
    if not validate(l, idx, idy, visited):
        return 0
    print("ds", l[idx][idy],"count" ,num)
    if l[idx][idy] == 1:
        num += 1
    visited.add((idx,idy))
    x = dfs(l, idx + 1, idy, visited, num)  + dfs(l, idx  -1, idy, visited, num) + dfs(l, idx, idy + 1, visited, num) + dfs(l, idx, idy - 1, visited, num)
    if x == 0:
        res = num
    return num
res = 0

def backsolve_dfs(l, idx, idy, visited):
    if not validate(l, idx, idy, visited):
        return 0
    # print("ds", l[idx][idy])
    
    visited.add((idx,idy))
    ur_num = backsolve_dfs(l, idx + 1, idy, visited)  + backsolve_dfs(l, idx  -1, idy, visited) + backsolve_dfs(l, idx, idy + 1, visited) + backsolve_dfs(l, idx, idy - 1, visited)

    if l[idx][idy] == 1:
        return ur_num + 1
    return ur_num
if __name__ == '__main__':
    global res
    l = [[1,2,1], [4, 1, 6], [7, 1, 9]]
    visited = set()
    # dfs(l, 0,0, visited, 0)
    # print(res)
    print(backsolve_dfs(l, 0,0, visited))
# Find the largest value on each level of a binary tree.
# TODO
from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def find_level_average(root):
    '''
    TC : O(N)
    SC: O(N)
    '''
    result = []
    q = deque()
    q.append(root)

    while q:
        l = len(q)
        if q:
            x = [i.val for i in q]
            result.append(sum(x)/ len(x))
            
        for _ in range(l):
            r = q.popleft()

            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)

    return result

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.left.right = TreeNode(2)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    r1 = find_level_average(root)
    print(f"level averages are : {r1}")

    assert r1 == [12.0, 4.0, 6.5]

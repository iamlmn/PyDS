# Find the minimum depth of a binary tree. 
# The minimum depth is the number of nodes along the shortest path from the root node to the nearest leaf node.


from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def getMinDepth(root):
    minDepth = -1
    q = deque()
    q.append(root)
    depth = 0
    pl = 1
    while q:
        l = len(q)
        depth += 1
        
        for _ in range(l):
            r = q.popleft()
            if r.left is None and r.right is None:
                return depth
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
        pl = l
    return mindDepth
            

def getMaxDepth(root):

    q = deque()
    if root is not None:
        maxDepth = 0
        q.append(root)
    else:
        return -1
    while q:
        l = len(q)
        maxDepth += 1
        for _ in range(l):
            r = q.popleft()
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
    return maxDepth

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    r1 = getMinDepth(root)
    r12 = getMaxDepth(root)
    print(f"The minimum depth is {r1}")
    print(f"The maximum depth is {r12}")
    root.left.left = TreeNode(9)
    root.right.left.left = TreeNode(11)
    r2 = getMinDepth(root)
    r21 = getMaxDepth(root)
    print(f"The minimum depth is {r2}")
    print(f"The maximum depth is {r21}")

    assert r1 == 2
    assert r2 == 3
    assert r12 == 3
    assert r21 == 4
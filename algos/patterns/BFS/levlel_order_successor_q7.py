# Given a binary tree and a node, find the level order successor of the given node in the tree. 
# The level order successor is the node that appears right after the given node in the level order traversal.


from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def get_level_order_successor(root, element):
    minDepth = -1
    q = deque()
    q.append(root)
    depth = 0
    flag = 0 # set when the element is found
    res = None
    while q:
        l = len(q)
        depth += 1
        
        for _ in range(l):
            r = q.popleft()
            if r.val == element:
                flag = 1
            if r.left:
                q.append(r.left)

            if r.right:
                q.append(r.right)

            if flag:
                return q[0]
    return -1

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    r1 = get_level_order_successor(root, 12)
    r2 = get_level_order_successor(root, 9)
    print(r1.val)
    print(r2.val)
    assert r1.val == 7
    assert r2.val == 10


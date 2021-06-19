# # Problem statement 1


# Given a binary tree, populate an array to represent its level-by-level traversal. 
# You should populate the values of all nodes of each level from left to right in separate sub-arrays.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    '''
    TC : O(N)
    SC : O(N)
    '''
    result = []
    q = deque()
    q.appendleft(root)
    while q:
        l = len(q) # get the lenght of deque
        if q: # insert elements before popping every element from that level
            result.append([i.val for i in (q)][::-1]) # reverse it so that it comes in left to right order.

        for _ in range(l):
            r = q.pop()
            if r.left:
                q.appendleft(r.left)
            if r.right:
                q.appendleft(r.right)
    return result


if __name__ == '__main__':

    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    r1 = traverse(root)
    print(f"Level order traversal : {r1}")
    assert r1 == [[12], [7, 1], [9, 10, 5]]
    
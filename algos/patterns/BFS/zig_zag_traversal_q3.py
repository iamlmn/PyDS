# Given a binary tree, populate an array to represent its zigzag level order traversal. 
#  You should populate the values of all nodes of the first level from left to right, 
# then right to left for the next level and keep alternating in the same manner for the following levels.


from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

def traverse(root):
    result = []
    q = deque()
    q.append(root)
    zig_zag_flag = 0
    while q:
        l = len(q)
        if q:
            if not zig_zag_flag:
                result.append([i.val for i in q][::-1])
                zig_zag_flag = 1
            else:
                result.append([i.val for i in q])
                zig_zag_flag = 0

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

    root.right.left.left = TreeNode(20)
    root.right.left.right = TreeNode(17)
    r1 = traverse(root)
    print(f"Zig Zag Traversal {r1}")
    assert r1 == [[12], [1, 7], [9, 10, 5], [17, 20]]
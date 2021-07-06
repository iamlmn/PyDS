# Given a binary tree and a number ‘S’, 
# find if the tree has a path from root-to-leaf such that the sum of all the node values of that path equals ‘S’.

# [1, 2, 3, 4, 5, 6, 7]
#  S: 10 Output: trueExplaination: The path with sum '10' is highlighted

# 12, 7, 1, 9, Null, 10, 5
# s:23 - true
# # s: 16 False

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def has_path(root, s, ts=0):
    if root is not None:
        ts += root.val
        if root.left is None and root.right is None:
            if s == ts:
                print("FOUND")
                return True
        return has_path(root.left, s, ts) or has_path(root.right, s, ts)
    else:
        return False
if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)

    print("Tree has path: " + str(has_path(root, 23, 0 )))
    print("Tree has path: " + str(has_path(root, 16, 0)))
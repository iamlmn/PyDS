# Right View of a Binary Tree (easy) #
# Given a binary tree, return an array containing nodes in its right view. 
# The right view of a binary tree is the set of nodes visible when the tree is seen from the right side.



from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right= None, None


def tree_right_view(root):
    result = []
    q = deque()
    q.append(root)

    while q:
        l = len(q)

        for i in range(l):
            r = q.popleft()
            if i == len(l) - 1:
                result.append(r.val)
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
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root.left.left.left = TreeNode(3)

    result = tree_right_view(root)
    print(f"Tree right view : {result}")


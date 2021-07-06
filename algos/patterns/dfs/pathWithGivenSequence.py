# Path With Given Sequence

# Given a binary tree and a number sequence, find if the sequence is present as a root-to-leaf path in the given tree.

#Example - 1
# Sequence - [1, 9, 9] 

class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    
def find_path(node, sequence,stack=[]):
    if node is None:
        return False
    stack.append(node.val)
    
    if node.left is None and node.right is None:
        print(stack, sequence)
        # leaf node
        if stack == sequence:
            return True
            
    c = find_path(node.left, sequence,stack) or find_path(node.right, sequence,stack)
    stack.pop()
    return c


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(0)
    root.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(5)

    print("Tree has path sequence: " + str(find_path(root, [1, 0, 7])))
    print("Tree has path sequence: " + str(find_path(root, [1, 1, 6])))

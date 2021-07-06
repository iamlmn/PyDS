class TreeNode:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def find_paths(node, targetSum, result=[], stack=[], currentSum=0):
    '''
    TC: O(N) 
    SC: O(N)
    '''
    if node:
        currentSum += node.val
        stack.append(node.val)
        if node.left is None and node.right is None:
            if currentSum == targetSum:
                result.append(list(stack))
        
        if node.left:
            find_paths(node.left, targetSum, result, stack, currentSum)
        if node.right:
            find_paths(node.right, targetSum, result, stack, currentSum)

        stack.pop()
    return result


if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    targetSum = 23

    print("Tree path with sum:" + str(targetSum) + ":" + str(find_paths(root, targetSum)))
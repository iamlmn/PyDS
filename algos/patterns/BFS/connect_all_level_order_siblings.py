# Connect All Level Order Siblings (medium) #
# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to the first node of the next level.

from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    # tree traversal using 'next' pointer.
    def print_tree(self):
        print("Traversal using 'next' pointer: ", end='')
        current = self
        while current:
            print(str(current.val) + " ", end='')
            current = current.next

def connect_all_siblings(root):
    '''
    TC : O(N)
    SC : O(N)
    '''
    q = deque()
    q.append(root)

    while q:
        l = len(q)
        for _ in range(l):
            r = q.popleft()
            
            if r.left:
                q.append(r.left)
            if r.right:
                q.append(r.right)
            if q:
                r.next = q[0]
            else:
                r.next = None
    return root

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    root = connect_all_siblings(root)

    root.print_tree()
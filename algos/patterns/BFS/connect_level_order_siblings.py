# Given a binary tree, connect each node with its level order successor. 
# The last node of each level should point to a null node.


from collections import deque

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right, self.next = None, None, None

    def print_level_order(self):
        nextLevelRoot = self
        while nextLevelRoot:
            current = nextLevelRoot
            nextLevelRoot = None

            while current:
                print(str(current.val) + " ", end='')
                if not nextLevelRoot:
                    if current.left:
                        nextLevelRoot = current.left
                    elif current.right:
                        nextLevelRoot = current.right
                current = current.next

            print()

def connect_level_order_siblings(root):
    q = deque()
    q.append(root)

    while q:
        l = len(q)

        for i in range(l):
            r = q.popleft()

            # None case
            if i == l - 1:
                r.next = None
            else:
                r.next = q[0]

            if r.left:
                q.append(r.left)

            if r.right:
                q.append(r.right)

        

if __name__ == '__main__':
    root = TreeNode(12)
    root.left = TreeNode(7)
    root.right = TreeNode(1)
    root.left.left = TreeNode(9)
    root.right.left = TreeNode(10)
    root.right.right = TreeNode(5)
    connect_level_order_siblings(root)

    print("Level order traversal using 'next' pointers : ")
    root.print_level_order()
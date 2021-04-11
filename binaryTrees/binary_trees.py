#Binary Tree using Linked representations.
from queues_linkedLists import QLinkedLists

class Node:
    __slot__ = 'element', 'left', 'right'

    def __init__(self, element, left=None, right=None):
        self.element = element
        self.left = left
        self.right = right


class BinaryTree:
    def __init__(self):
        self.root = None
    
    def makeTree(self, e, left, right):
        self.root = Node(e, left.root, right.root)


    def inorder(self, troot):
        if troot :
            self.inorder(troot.left)
            print(troot.element, end= ' ')
            self.inorder(troot.right)

    def preorder(self, troot):
        if troot :
            print(troot.element, end= ' ')
            self.preorder(troot.left)
            self.preorder(troot.right)


    def postorder(self, troot):
        if troot :
            self.postorder(troot.left)
            self.postorder(troot.right)
            print(troot.element, end= ' ')


    def levelorder(self):
        Q = QLinkedLists()
        t = self.root
        print(t.element, end= ' ')
        Q.enqueue(t)
        while not Q.isempty():
            t = Q.dequeue()
            if t.left:
                print(t.left.element, end= ' ')
                Q.enqueue(t.left)

            if t.right:
                print(t.right.element, end= ' ')
                Q.enqueue(t.right)

    def count_recursize(self, troot):
        if troot:
            x = self.count_recursize(troot.left)
            y = self.count_recursize(troot.right)
            return x + y + 1
        return 0

    def height(self, troot):
        if troot:
            x = self.height(troot.left)
            y = self.height(troot.right)
            if x> y:
                return x + 1
            else:
                return y + 1
        return 0




if __name__ == '__main__':
    x = BinaryTree()
    y = BinaryTree()
    z = BinaryTree()
    a = BinaryTree()

    x.makeTree(20, a, a)
    y.makeTree(30, a, a)
    z.makeTree(10, x, y)

    print("\n In-Order traversal")
    z.inorder(z.root)
    print("\n Pre Order traversal")
    z.preorder(z.root)
    print("\n Post Order traversal")
    z.postorder(z.root)

    import gc
    gc.collect()

    t = BinaryTree()
    r = BinaryTree()
    s = BinaryTree()
    x = BinaryTree()
    y = BinaryTree()
    z = BinaryTree()
    a = BinaryTree()

    x.makeTree(40, a, a)
    y.makeTree(60, a, a)
    z.makeTree(20, x, a)
    r.makeTree(50, a, y)
    s.makeTree(30, r, a)
    
    t.makeTree(10, z, s)

    print("\n In-Order traversal")
    t.inorder(t.root)
    print("\n Pre Order traversal")
    t.preorder(t.root)
    print("\n Post Order traversal")
    t.postorder(t.root)

    print("\n Level Order traversal")
    t.levelorder()
    print()
    print(f"Count of Binary Tree : {t.count_recursize(t.root)}")


    print(f"Height of the tree : {t.height(t.root) - 1} ")
    
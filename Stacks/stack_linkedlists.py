# LIFO Stack DS using Python Lists (Arrays)

class Node:
    __slot__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next
    
class StacksLinkedList:

    def __init__(self):
        self.top = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0

    def display(self):
        p = self.top
        while p:
            print(p.element, end = '-->')
            p = p.next
        print()

    def push(self, element):
        newest = Node(element, None)
        if self.isempty():
            self.top = newest
        else:
            newest.next = self.top
            self.top = newest
        self.size += 1


    def pop(self):
        if not self.isempty():
            e = self.top.element
            self.top = self.top.next
            self.size -=  1
            return e
        else:
            print("nO element to pop")
            return


    def peek(self):
        if self.isempty():
            print("Stack is empty.")
            return
        return self.top.element


if __name__ == '__main__':
    print("Stacks implemented with Lineked Lists.")
    S = StacksLinkedList()
    S.push(5)
    S.push(3)
    print("Length :", len(S))
    S.display()
    print(S.pop())
    print(S.isempty())
    S.display()
    print(S.pop())
    print(S.isempty())
    S.display()
    S.push(7)
    S.push(9)
    S.push(1)
    S.display()
    print(S.peek())
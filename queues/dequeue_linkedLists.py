class Node:
    def __init__(self, element, next):
        self.element = element
        self.next  = next
class DQ:
    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0

    def __len__(self):
        return self.size

    def isEmpty(self):
        return self.size == 0

    def display(self):
        p = self.front 
        while p:
            print(p.element, end= '-->')
            p = p.next

        print()

    def addFirst(self, element):
     
        newest = Node(element, None)
        if self.isEmpty():
            self.front = newest
            self.rear = newest
        else:
            newest.next = self.front
            self.front = newest
        self.size += 1


    def addLast(self, element):
        newest = Node(element, None)
        if self.isEmpty():
            self.front = newest
            
        else:
            self.rear.next = newest
        self.rear = newest
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            print("Queue is empty")
            return
        else:
            e = self.front.element
            self.front = self.front.next
        self.size -= 1
        return e

    def removeLast(self):
        if self.isEmpty():
            print("Queue is empty!")
            return 
        # else:
        p = self.front
        i = 1
        while i < len(self) - 1:
            p = p.next
            i = i + 1
        self.rear = p
        
        p = p.next
        e = p.element
        # p.next = None
        self.rear.next = None
        self.size -= 1
        return e

    
    def first(self):
        if self.isEmpty():
            print("DeQueue is empty")
            return
        return self.front.element

    def last(self):
        if self.isEmpty():
            print("DeQueue is empty")
            return
        return self.rear.element

if __name__ == '__main__':
    Q = DQ()
    Q.addFirst(5)
    Q.addFirst(3)
    Q.addLast(7)
    Q.addLast(12)
    Q.display()
    print(f"Length : {len(Q)}")
    print("Remove First",  Q.removeFirst())
    print("Remove Last",  Q.removeLast())
    Q.display()
    print(f"First element : {Q.first()}")
    print(f"Last element : {Q.last()}")

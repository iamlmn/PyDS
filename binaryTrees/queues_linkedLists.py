class Node:
    __slot__ = 'element', 'next'

    def __init__(self, element, next):
        self.element = element
        self.next = next


class QLinkedLists:

    def __init__(self):
        self.front = None
        self.rear = None
        self.size = 0


    def __len__(self):
        return self.size
    

    def isempty(self):
        return (self.size == 0)

    def display(self):
        p = self.front
        while p:
            print(p.element, end= '-->')
            p = p.next
        print()

    def peek(self):
        if self.isempty():
            print("Queue is empty!")
            return
        return self.front.element

    def enqueue(self, element):
        newest = Node(element, None)
        if self.isempty():
            self.front = newest
        else:
            self.rear.next = newest
        self.rear = newest

        self.size += 1
    

    def dequeue(self):
        if self.isempty():
            print("Empty Queue!")
            return
        else:
            e = self.front.element
            self.front = self.front.next
        self.size -= 1
        return e


if __name__ == '__main__':
    Q = QLinkedLists()
    Q.enqueue(5)
    Q.enqueue(15)
    Q.enqueue(115)
    Q.display()
    print("Running Dequeue")
    Q.dequeue()
    Q.display()
    print("Quick peek to Queue->", Q.peek())
    Q.dequeue()
    Q.display()
    print("Quick peek to Queue->", Q.peek())


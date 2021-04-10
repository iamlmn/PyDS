class DQ:
    def __init__(self):
        self.dq = []

    def __len__(self):
        return len(self.dq)

    def isempty(self):
        return len(self.dq) == 0

    def display(self):
        print(self.dq)

    def first(self):
        return self.dq[0]

    def last(self):
        return self.dq[-1]

    def addFirst(self, element):
        self.dq = [element] + self.dq
    
    def addLast(self, element):
        self.dq.append(element)

    def removeFirst(self):
        if self.isempty():
            print("Queue is empty!")
            return 
        return self.dq.pop(0)
    
    def removeLast(self):
        if self.isempty():
            print("Queue is empty!")
            return 
        return self.dq.pop()


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

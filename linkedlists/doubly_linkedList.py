class Node:
    __slot__ = 'element' , 'prev', 'next'
    def __init__(self, element, next, prev):
        self.element = element
        self.next = next
        self.prev = prev


class DLinkedLists:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def __len__(self):
        return self.size
    
    def isempty(self):
        return self.size == 0 


    def display(self):
        p = self.head
        if self.isempty():
            print("List is empty.")
            return
        while p:
            print(p.element, end='<=>')
            p = p.next
        print()

    def displayrev(self):
        p = self.tail
        while p:
            print(p.element, end="<--")
            p = p.prev
        print()


    def addLast(self, element):
        
        p = self.tail
        newest = Node(element, None, None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            newest.prev = self.tail
            self.tail = newest
        self.size += 1


    def addFirst(self, element):
        newest = Node(element, None, None)
        if self.isempty():
            self.head = newest
            self.tail = newest
            
        else:
            newest.next = self.head
            self.head.prev = newest
            self.head = newest
        self.size += 1
    

    def addAny(self, element):
        p = self.head
        newest = Node(element, None, None)
        if self.isempty():
            print("List is empty.")
            return
        i = 1
        while i < len(self) - 1:
            p = p.next
            i += 1 
        newest.next = p.next
        newest.prev = p
        p.next.prev = newest
        p.next = newest
        self.size += 1

    def removeFirst(self):
        if self.isempty():
            print("List is empty")
            return
        e = self.head.element
        self.head.prev = None
        self.head = self.head.next
        self.size -= 1
        if self.isempty():
            self.head = None
            self.tail = None
        return e
        
    
    def removeLast(self):
        if self.isempty():
            print("List is empty!")
            return
        e = self.tail.element
        self.tail.prev.next = None
        self.tail.prev = None
        self.size -= 1
        if self.isempty():
            self.head = None
            self.tail = None
        return e
        

    def removeAny(self, position):
        p = self.head
        i = 1
        while i < (position - 1):
            p = p.next
            i = i + 1
        e = p.next.element
        p.next = p.next.next
        p.next.prev = p
        self.size -= 1
        if self.isempty():
            self.head = None
            self.tail = None
        return e

    def search():
        pass


if __name__ == '__main__':
    L = DLinkedLists()
    L.addLast(7)
    L.addLast(4)
    L.addLast(12)
    L.addLast(8)
    L.addLast(3)
    L.display()
    print('Size:',len(L))
    ele = L.removeAny(3)
    L.display()
    print('Size:',len(L))
    print('Removed Element:',ele)
    L.displayrev()
    L.display()

    ele = L.removeFirst()
    L.display()
    print('Size:',len(L))
    print('Removed Element:',ele)

    ele = L.removeLast()
    L.display()
    print('Size:',len(L))
    print('Removed Element:',ele)
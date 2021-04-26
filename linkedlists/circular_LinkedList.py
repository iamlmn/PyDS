class Node:
    __slot__ = 'element', 'next' # for better memory arrangment. 
    
    def __init__(self, element, next):
        self.element = element
        self.next = next


class CircularLinkedList:
    # Linear Linked List.

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
        i = 0
        while i < len(self):
            print(p.element, end='-->')
            p = p.next
            i = i+1
        print()
        


    def addLast(self, element):
        '''
        Space : O(1)
        Time : O(1)
        '''
        newest = Node(element, None)
        if self.isempty():
            newest.next = newest
            self.head = newest
        else:
            newest.next = self.head
            self.tail.next = newest

        self.tail = newest
        self.size += 1


    
    def addFirst(self, element):
        p  = self.head
        newest = Node(element, None)
        if self.isempty():
            newest.next = newest
        else:
            self.tail.next = newest
            newest.next = self.head
        self.head = newest
        self.size += 1



    
    def addAny(self, element, position):
        p = self.head
        newest = Node(element, None)
        i = 1

        while i < position - 1:
            p = p.next
            i += 1

        newest.next = p.next 
        p.next = newest

        self.size += 1

    def removeFirst(self):
        p = self.head
        if self.isempty():
            print("Unable to delete first element, List is already empty.")
            return
        e = self.head.element
        self.head = self.head.next
        self.tail.next = self.head
        self.size -= 1

        if self.isempty():
            self.head = None
            self.tail = None
        return e 
    
    def removeLast(self):
        if self.isempty():
            print("Unable to delete first element, List is already empty.")
            return
        p = self.head
        
        while p.next.next != self.head:
            p = p.next
        e = p.next.element
        p.next = self.head
        self.size -= 1

        if self.isempty():
            self.head = None
            self.tail = None     

        return e
   

    def removeAny(self, position):
        p = self.head
        i = 1
        while i < position - 1:
            p = p.next
            i += 1 
        e = p.next.element
        p.next = p.next.next
        self.size -= 1
        return e

    def search(self, element):
        if self.isempty():
            print("List is empty!")
            return 
        p = self.head
        i = 1
        while i <= len(self):
            if p.element == element:
                print(f"{element} found at pos - {i}")
                return i
            p = p.next
            i += 1
        return -1


    def reverese(self):
        pass
    
    def sort(self):
        pass


if __name__ == '__main__':
    
    C = CircularLinkedList()
    C.addLast(7)
    C.addLast(4)
    C.addLast(12)
    C.addLast(8)
    C.addLast(3)
    C.display()
    print('Size:',len(C))
    ele = C.removeAny(3)
    C.display()
    print('Size:',len(C))
    print('Removed Element:',ele)

    # Remove first
    ele = C.removeFirst()
    C.display()
    print('Size:',len(C))
    print('Removed Element:',ele)

    # Remove Last
    ele = C.removeLast()
    C.display()
    print('Size:',len(C))
    print('Removed Element:',ele)


    # Remove Last
    C.display()
    print(C.search(8))
    print(C.search(21))


    
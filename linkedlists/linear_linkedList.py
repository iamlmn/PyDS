class _Node:
    __slot__ = 'element', 'next' # for better memory arrangment. 
    
    def __init__(self, element, next):
        self.element = element
        self.next = next


class LinkedList:
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
        '''
        Space : O(1)
        Time : O(m)
        '''
        if self.isempty():
            print("List is empty!")
        p = self.head
        while p:
            print(p.element,end='-->')
            p = p.next
        print()


    def addLast(self, element):
        '''
        Space : O(1)
        Time : O(1)
        '''
        newest = _Node(element, None)
        if self.isempty():
            self.head = newest
            self.tail = newest
        else:
            self.tail.next = newest
            self.tail = newest
        self.size += 1


    
    def addFirst(self, element):
        '''
        Space : O(1)
        Time : O(1)
        '''
        newest = _Node(element, self.head) # Trying with self.head, mostly will be passing None.
        if isempty():
            self.head = newest
            self.tail = newest
        else:
            # newest._next = self._head # 
            self.head = newest
        self.size += 1
    
    def addAny(self, element, position):
        '''
        Space : O(1)
        Time : O(n)
        '''
        p = self.head
        i = 1
        newest = _Node(element, None)
        assert postion < len(self)
        while i < position - 1:
            p = p.next
            i = i + 1
        newest.next = p.next
        p.next = newest
        self.size += 1
    
    def removeLast(self):
        '''
        Space : O(1)
        Time : O(n)
        '''
        if self.isempty():
            print("List is empty")
            return
        p = self.head
        i = 1
        while i < len(self) - 1:
            p = p.next
            i += 1
        
        e = self.tail.element
        self.tail = p
        self.tail.next = None
        self.size -= 1
        return e

    def removeFirst(self):
        '''
        Space : O(1)
        Time : O(1)
        '''
        if self.isempty():
            print("List is empty")
            return
        e = self.head.element
        self.head = self.head.next
        self.size -= 1

        if self.isempty():
            self._tail = None
        return e



    def removeAny(self, position):
        '''
        Space : O(1)
        Time : O(n)
        '''
        if self.isempty():
            print("List is empty")
            return

        p = self.head
        i = 1
    
        while i < position - 1:
            p = p.next
            i += 1
        if i == len(self) - 1:
            self.tail = p # make tail ur last but before element.
            e = p.next.e
        else:
            p.next = p.next.next

        e = p.next.element
        self.size -= 1

        return e

        


    def search(self, element):
        '''
        Space : O(1)
        Time : O(n)
        '''
        if self.isempty():
            print("List is empty!")
            return 

        p = self.head
        i = 0
        while p:
            if p.element == element:
                print(f"{element} found at pos - {i}")
                return i
            p = p.next
            i = i + 1
        return -1

                

    def reverse(self):
        '''
        Space : O(1)
        Time : O(n)
        '''
        p = self.head
        prev = None
        while p is not None:
            next = p.next
            p.next = prev
            prev = p
            p = next
        self.head = prev

    def recursiveUtil(self, curr, prev):
        if curr.next is None:  # If last node mark it head
            self.head = curr    # Update next to prev node
            curr.next = prev
            return

        next = curr.next  # Save curr.next node for recursive call
        curr.next = prev    # And update next
        self.recursiveUtil(next, curr)

    def recursive_reverse(self):
        '''
        Space : O(n)
        Time : O(n)
        '''

        if self.head is None:
            return
        self.recursiveUtil(self.head, None)
        


    def stack_reverse(self):
        pass

            

    
    def sort(self):
        pass


if __name__ == '__main__':
    L = LinkedList()
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
    L.search(3)
    print()
    
    # regular reverse test case
    print("Given Linked List")
    L.display()
    L.reverse()
    print("\nReversed Linked List")
    L.display()
    print()

    # recursive_reverse
    print("Given Linked List")
    L.display()
    L.recursive_reverse()
    print("\nRecursice reversed Linked List")
    L.display()
    print()

    # 2 element reverese
    L.removeFirst()
    L.removeLast()
    print("2 element reverese \n___________________ \n Given Linked List")
    L.display()
    L.reverse()
    print("\nReversed Linked List")
    L.display()
    print()

    # single list reversal
    L.removeLast()
    print("single list reversal \n___________________ \n Given Linked List")
    L.display()
    L.reverse()
    print("\nReversed Linked List")
    L.display()
    print()
    # Empty linked list reversal
    L.removeFirst()
    print("Given Linked List")
    L.display()
    L.reverse()
    print("\nReversed Linked List")
    L.display()
    print()
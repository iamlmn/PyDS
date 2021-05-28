class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next

def reverse(head):
    current = head
    prev = None

    while current is not None:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
    
    return prev

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)

    print("Nodes of original LinkedList are : ", head.print_list())
    newhead = reverse(head)
    print("Nodes of reveresed LinkedList are : ", newhead.print_list())
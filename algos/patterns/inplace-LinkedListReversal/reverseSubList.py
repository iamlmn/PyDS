# Given the head of a LinkedList and two positions ‘p’ and ‘q’, reverse the LinkedList from position ‘p’ to ‘q’.


class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next


def reverse_sublist(head, p, q):
    current = head
    prev = None
    i = 1

    if p == q:
        return head

    while i < p:
        prev = current  
        current = current.next
        i += 1

    last_node_of_first_subpart = prev
    to_be_last_node = current
    print(i)
    # exit(1)
    while current is not None and i <= q:
        _next = current.next
        current.next = prev
        prev = current
        current = _next
        i += 1

    to_be_last_node.next = current
    
    if last_node_of_first_subpart is not None:
        last_node_of_first_subpart.next = prev
    else:
        head = prev

    return head




if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)

    print("Nodes of original LinkedList are : ", head.print_list())
    newhead = reverse_sublist(head, 2, 4)
    print("Nodes of reveresed LinkedList are : ", newhead.print_list())
# Problem Statement #
# Given the head of a LinkedList and a number ‘k’, reverse every ‘k’ sized sub-list starting from the head.

# If, in the end, you are left with a sub-list with less than ‘k’ elements, reverse it too.



class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='->')
            temp = temp.next

def reverseHelper(head, current, prev, k):
    
        # return elementReversed, head
    return elementReversed, last_node_of_first_subpart, last_to_be_node


def reverse_every_k_elements(head, k):
    c = 1
    #edge case
    if k == 1:
        return head
    
    prev = None
    current = head
    while current is not None and c <= k:
        print("ASd")
        elementReversed = 1
        last_node_of_first_subpart = prev
        last_to_be_node = current

        while current is not None and elementReversed <= k:
            _next = current.next 
            current.next = prev
            prev = current
            current = _next
            elementReversed += 1

        last_to_be_node.next = current
        if last_node_of_first_subpart is not None:
            last_node_of_first_subpart.next = prev
        else:
            head = prev
        # current = current.next
        prev = last_to_be_node
        c = 1
        if c > k:
            return head
        # break
    return head


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)
    head.next.next.next.next.next.next = Node(7)
    head.next.next.next.next.next.next.next = Node(8)

    print("Nodes of original LinkedList are : ", head.print_list())
    newhead = reverse_every_k_elements(head, 3)
    print("Nodes of reveresed LinkedList are : ", newhead.print_list())
# Reverse alternating K-element Sub-list (medium) #
# Given the head of a LinkedList and a number ‘k’, reverse every alternating ‘k’ sized sub-list starting from the head.

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
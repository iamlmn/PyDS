# Rearrange a LinkedList (medium) #
# Given the head of a Singly LinkedList, write a method to modify the LinkedList such that the nodes from the second half of the LinkedList are inserted alternately to the nodes from the first half in reverse order. So if the LinkedList has nodes 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> null, your method should return 1 -> 6 -> 2 -> 5 -> 3 -> 4 -> null.

# Your algorithm should not use any extra space and the input LinkedList should be modified in-place.

# Example 1:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> 12 -> null
# Output: 2 -> 12 -> 4 -> 10 -> 6 -> 8 -> null 
# Example 2:

# Input: 2 -> 4 -> 6 -> 8 -> 10 -> null
# Output: 2 -> 10 -> 4 -> 8 -> 6 -> null
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self

        while temp is not None:
            print(str(temp.value) + " ", end='')
            temp = temp.next
        print()

def getMid(head):
    slow, fast = head, head
    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next
    
    return slow


def reArrangeLinkedList(head):

    # getMid
    mid = getMid(head)

    #reverse second half
    mid_copy = mid
    print(mid.value)
    ptr2 = reverse(mid_copy)

    
    ptr1 = head
    # ptr2 = mid
    # second ptr2 start from mid, ptr1 from start, use insrtAfter node and insert elemetns untill second.next = None.
    while ptr1 is not None and ptr2 is not None:
        temp = ptr1.next
        ptr1.next = ptr2
        ptr1  = temp

        temp = ptr2.next
        ptr2.next = ptr1
        ptr2 = temp

    # set the next of last node to None
    if ptr1 is not None:
        ptr1.next = None

        
def reverse(head):
    prev = None
    while head is not None:
        next = head.next
        head.next = prev
        prev = head
        head = next
    return prev

if __name__ == '__main__':
    head = Node(2)
    head.next = Node(4)
    head.next.next = Node(6)
    head.next.next.next = Node(8)
    head.next.next.next.next = Node(10)
    head.next.next.next.next.next = Node(12)
    reArrangeLinkedList(head)
    head.print_list()
    

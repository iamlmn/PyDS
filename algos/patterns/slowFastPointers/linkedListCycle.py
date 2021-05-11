# Given the head of a Singly LinkedList, write a function to determine if the LinkedList has a cycle in it or not.
# Time and Space Complexity: The above algorithm runs in O(N)O(N) time complexity and O(1)O(1) space complexity.

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next


def has_cycle(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next
        if slow == fast:
            return True
    return False


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList has cycle: " + str(has_cycle(head)))
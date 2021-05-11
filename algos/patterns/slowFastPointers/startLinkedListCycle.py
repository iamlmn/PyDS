# Given the head of a Singly LinkedList that contains a cycle, write a function to find the starting node of the cycle.
class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

    def print_list(self):
        temp = self
        while temp is not None:
            print(temp.value, end='')
            temp = temp.next

        print()

def find_cycle_start(head):
    fast,slow = head, head
    while fast is not None and fast.next is not None:
        fast = fast.next.next
        slow = slow.next

        if slow == fast:
            cycle_length = get_cycle_length(head, slow)
            break
    return find_start_of_cycle(head, cycle_length)

def find_start_of_cycle(head, cycle_length):
    pt1, pt2 = head, head
    while cycle_length:
        pt2 = pt2.next
        cycle_length -= 1
    while pt1 != pt2:
        pt1 = pt1.next
        pt2 = pt2.next

    return pt1.value

def get_cycle_length(head, slow):
    pt1 = slow
    cycle_length = 0

    while True:
        pt1 = pt1.next
        cycle_length += 1
        if pt1 == slow:
            break

    return cycle_length


if __name__ == '__main__':
    head = Node(1)
    head.next = Node(2)
    head.next.next = Node(3)
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(5)
    head.next.next.next.next.next = Node(6)

    head.next.next.next.next.next.next = head.next.next
    print("LinkedList cycle starts at: " + str(find_cycle_start(head)))

    head.next.next.next.next.next.next = head.next.next.next
    print("LinkedList cycle starts at: " + str(find_cycle_start(head)))

    head.next.next.next.next.next.next = head
    print("LinkedList cycle starts at: " + str(find_cycle_start(head)))
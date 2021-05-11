# Given the head of a Singly LinkedList, write a method to check if the LinkedList is a palindrome or not.

# Your algorithm should use constant space and the input LinkedList should be in the original form once the algorithm is finished. The algorithm should have O(N)O(N) time complexity where ‘N’ is the number of nodes in the LinkedList.

# Example 1:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> null
# Output: true
# Example 2:

# Input: 2 -> 4 -> 6 -> 4 -> 2 -> 2 -> null
# Output: false

class Node:
    def __init__(self, value, next=None):
        self.value = value
        self.next = next

def getMid(head):
    slow, fast = head, head

    while fast is not None and fast.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow

def isPalindrome(head):
    # Find mid
    mid = getMid(head)
    # print(mid.value)
    # reverse mid to end
    mid = reverse(mid)
    # compare first half and second half
    head_second = mid
    while head is not None and head_second is not None:
        if head.value != head_second.value:
            break
        head = head.next
        head_second = head_second.next
    # reset second half by reverising again
    reverse(mid)

    if head_second is not None:
        return False
    return True
def reverse(head):
    t = head 
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
    head.next.next.next = Node(4)
    head.next.next.next.next = Node(2)

    print("Is palindrome: " + str(isPalindrome(head)))
    head.next.next.next.next.next = Node(2)
    print("Is palindrome: " + str(isPalindrome(head)))
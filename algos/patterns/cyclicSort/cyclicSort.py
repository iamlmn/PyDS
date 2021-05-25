# We are given an array containing ‘n’ objects. Each object, when created, was assigned a unique number from 1 to ‘n’ based on their creation sequence. This means that the object with sequence number ‘3’ was created just before the object with sequence number ‘4’.

# Write a function to sort the objects in-place on their creation sequence number in O(n)O(n) and without any extra space. For simplicity, let’s assume we are passed an integer array containing only the sequence numbers, though each number is actually an object.

# Example 1:

# Input: [3, 1, 5, 4, 2]
# Output: [1, 2, 3, 4, 5]
# Example 2:

# Input: [2, 6, 4, 3, 1, 5]
# Output: [1, 2, 3, 4, 5, 6]
# Example 3:

# Input: [1, 5, 6, 4, 3, 2]
# Output: [1, 2, 3, 4, 5, 6]

def swap(i, j, array):
    array[i], array[j] = array[j], array[i]


def cyclicSort(array):
    i = 0
    while i < (len(array)):
        if array[i] == i +1:
            i += 1
        else:
            swap(i, array[i] - 1, array)
    return array
    

if __name__ == '__main__':
    array1 = [3, 1, 5, 4, 2]
    array2 = [2, 6, 4, 3, 1, 5]
    array3 = [1, 5, 6, 4, 3, 2]

    out1 = [1, 2, 3, 4, 5]
    out23 = [1, 2, 3, 4, 5, 6]

    r1 = cyclicSort(array1)
    r2 = cyclicSort(array2)
    r3 = cyclicSort(array3)

    print(r1, r2, r3)
    assert out1 == r1
    assert out23 == r2
    assert out23 == r3





# How do we find the rotation count of a sorted and rotated array that has duplicates too?

# The above code will fail on the following example!

# Example 1:

# Input: [3, 3, 7, 3]
# Output: 3
# Explanation: The array has been rotated 3 times


def get_rotation_count(array):
    s = 0 
    e = len(array) - 1

    while s < e: 
        m = (s + e)//2  

        if m < e and array[m] > array[m + 1]:
            return m + 1

        if m > s and array[m - 1] > array[m]:
            return m
    
        if array[s] == array[m] and array[m] == array[e]:
            if array[s] > array[s  + 1]:
                return s + 1
            s += 1
            if array[e] < array[e - 1]:
                return e 
            e -= 1
            
        elif array[m] >= array[s]:
            s = m + 1
        else:
            e = m - 1
    return 0

if __name__ == '__main__':
    arr1 = [3, 3, 7, 3]
    arr2 = [3, 7,3, 3]
    arr3 = [1, 3, 8, 10]

    r1 = get_rotation_count(arr1)
    r2 = get_rotation_count(arr2)
    r3 = get_rotation_count(arr3)

    print(r1) 
    print(r2)
    print(r3)

    assert r1 == 3
    assert r2 == 2
    assert r3 == 0
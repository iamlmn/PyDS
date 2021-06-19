# Given an array of lowercase letters sorted in ascending order, find the smallest letter in the given array greater than a given ‘key’.

# Assume the given array is a circular list, which means that the last letter is assumed to be connected with the first letter. This also means that the smallest letter in the given array is greater than the last letter of the array and is also the first letter of the array.

# Write a function to return the next letter of the given ‘key’.

# Example 1:

# Input: ['a', 'c', 'f', 'h'], key = 'f'
# Output: 'h'
# Explanation: The smallest letter greater than 'f' is 'h' in the given array.
# Example 2:

# Input: ['a', 'c', 'f', 'h'], key = 'b'
# Output: 'c'
# Explanation: The smallest letter greater than 'b' is 'c'.
# Example 3:

# Input: ['a', 'c', 'f', 'h'], key = 'm'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'm' is 'a'.
# Example 4:

# Input: ['a', 'c', 'f', 'h'], key = 'h'
# Output: 'a'
# Explanation: As the array is assumed to be circular, the smallest letter greater than 'h' is 'a'.



def getNextLetter(arr, e):
    '''
    Time : O(logn)
    Space : O(1)
    '''
    left = 0
    right = len(arr) - 1

    while left <= right:
        
        mid = (left + right)//2
        if arr[mid] == e:
            print(f"Found at {mid}")
            if mid + 1 < len(arr):
                return arr[mid + 1]
            else:
                return arr[0]
        
        if (arr[mid]) > e:
            right = mid - 1      
            
        else:
            left = mid + 1

    return arr[left % len(arr)]

if __name__ == '__main__':
    arr1 =  ['a', 'c', 'f', 'h']
    arr2 = ['a', 'c', 'f', 'h']
    arr3 = ['a', 'c', 'f', 'h']
    arr4 = ['a', 'c', 'f', 'h']

    # elements

    e1 = 'f'
    e2 = 'b'
    e3 = 'm'
    e4 = 'h'

    r1 = getNextLetter(arr1, e1)
    r2 = getNextLetter(arr2, e2)
    r3 = getNextLetter(arr3, e3)
    print(r3)
    r4 = getNextLetter(arr4, e4)
    
    assert r1 == 'h'
    assert r2 == 'c'
    assert r3 == 'a'
    assert r4 == 'a'

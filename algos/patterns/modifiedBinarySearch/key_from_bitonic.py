# Given a Bitonic array, find if a given ‘key’ is present in it. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Write a function to return the index of the ‘key’. If the ‘key’ is not present, return -1.

# Example 1:

# Input: [1, 3, 8, 4, 3], key=4
# Output: 3
# Example 2:

# Input: [3, 8, 3, 1], key=8
# Output: 1
# Example 3:

# Input: [1, 3, 8, 12], key=12
# Output: 3
# Example 4:

# Input: [10, 9, 8], key=10
# Output: 0

def do_binary_search(array, start, end, e, asc_order=True):

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == e:
            return mid

        if array[mid] < e:
            if asc_order == True:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if asc_order == True:
                end = mid - 1
            else:
                start = mid + 1
    return 


def search_bitonic_array(array, key):
    # get the point where it starts to decrease.


    st = 0
    end = len(array) - 1

    while st < end:
        mid = (st + end) // 2
        if array[mid] > array[mid + 1]:
            end = mid 
        elif array[mid] <= array[mid + 1]:
            st = mid + 1
    
    change_point = st

    if array[change_point] == key:
        return change_point
    # 1. let the mid be end for first search and check for the value
    r1 = do_binary_search(array, 0, change_point, key )
    r2 = do_binary_search(array, change_point + 1, len(array) - 1, key, asc_order=False )
    # 2. Let the mid be start for second set of search.
    if r1 is None and r2 is None:
        return -1
    if r1:
        return r1
    return r2

if __name__ == '__main__':
    arr1 = [1, 3, 8, 4, 3]
    key1 = 4

    arr2 = [3, 8, 3, 1]
    key2 = 8

    arr3 = [1, 3, 8, 12]
    key3 = 12

    arr4 = [10, 9, 8]
    key4 = 10


    r1 = search_bitonic_array(arr1, key1)
    r2 = search_bitonic_array(arr2, key2)
    r3 = search_bitonic_array(arr3, key3)
    r4 = search_bitonic_array(arr4, key4)

    print(r1, r2, r3, r4)


    assert r1 == 3
    assert r2 == 1
    assert r3 == 3
    assert r4 == 0

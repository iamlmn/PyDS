 


def linear_search(array, key):
    index = 0
    while index < len(array):
        if array[index] == key:
            return index
        index +=1
    return -1




def binary_search_iterative(array, key):
    left = 0
    right = len(array) - 1
    # Array should be in sorted order.
    while left <= right:
        mid = (left + right )// 2
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            right = mid - 1
        elif key > array[mid]:
            left = mid + 1
    return -1


def binary_search_recursive(array, key, left, right):

    # Array should be in sorted order.
    if left > right:
        return -1
    else:
        mid = (left + right) // 2
        if array[mid] == key:
            return mid
        elif key < array[mid]:
            return binary_search_recursive(array, key, left, mid - 1)
        elif key > array[mid]:
            return binary_search_recursive(array, key, mid + 1, right)
    


if __name__ == '__main__':
    a = [84,  40, 87, 12, 21, 10]
    print("********* Linear search ***********")
    print("Time Complexity : O((1)")
    print("Space Complexity : O((n) ")
    print(linear_search(a, 21))
    print(linear_search(a, 211))
    x = [1, 2, 3, 5, 21, 63, 66]
    print("********* Binary search - iterative **********")
    print("Time Complexity : O((1)")
    print("Space Complexity : O((log(n)) ")
    print(binary_search_iterative(x, 21))
    print(binary_search_iterative(x, 211))
    print("********** Binary search - recursive **********")
    print("Time Complexity : O((log(n))  - recursion uses that much memory")
    print("Space Complexity : O((log(n))  ")
    print(binary_search_recursive(x, 21, 0, len(x) - 1))
    print(binary_search_recursive(x, 211, 0, len(x) - 1))
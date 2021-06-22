# Find the maximum value in a given Bitonic array. An array is considered bitonic if it is monotonically increasing and then monotonically decreasing. Monotonically increasing or decreasing means that for any index i in the array arr[i] != arr[i+1].

# Example 1:

# Input: [1, 3, 8, 12, 4, 2]
# Output: 12
# Explanation: The maximum number in the input bitonic array is '12'.
# Example 2:

# Input: [3, 8, 3, 1]
# Output: 8
# Example 3:

# Input: [1, 3, 8, 12]
# Output: 12
# Example 4:

# Input: [10, 9, 8]
# Output: 10

def get_bitonic_max(array):
    start = 0 
    end = len(array) - 1

    while start < end:
        mid = (start + end) // 2

        if array[mid] > array[mid + 1]:
            end = mid 
        elif array[mid] <= array[mid + 1]:
            start = mid + 1
    return array[start]

if __name__ == '__main__':
    arr1 = [1, 3, 8, 12, 4, 2]
    arr2 = [3, 8, 3, 1]
    arr3 = [1, 3, 8, 12]
    arr4 = [10, 9, 8]

    r1 = get_bitonic_max(arr1)
    r2 = get_bitonic_max(arr2)
    r3 = get_bitonic_max(arr3)
    r4 = get_bitonic_max(arr4)

    print(r1)
    print(r2)
    print(r3)
    print(r4)

    assert r1 == 12
    assert r2 == 8
    assert r3 == 12
    assert r4 == 10
# Given a sorted number array and two integers ‘K’ and ‘X’, 
# find ‘K’ closest numbers to ‘X’ in the array. Return the numbers in the sorted order. 
# # ‘X’ is not necessarily present in the array.

# Example 1:

# Input: [5, 6, 7, 8, 9], K = 3, X = 7
# Output: [6, 7, 8]
# Example 2:

# Input: [2, 4, 5, 6, 9], K = 3, X = 6
# Output: [4, 5, 6]
# Example 3:

# Input: [2, 4, 5, 6, 9], K = 3, X = 10
# Output: [5, 6, 9]
from heapq import *
def find_closest_elements(arr, k, x):
    minHeap = []
    for i in range(len(arr)):
        if i < k:
            heappush(minHeap, (-abs(arr[i] - x), arr[i]))
        else:
            if -(arr[i] - x) >= minHeap[0][0]:
                heappop(minHeap)
                heappush(minHeap, (-abs(arr[i] - x), arr[i]))
    return [i for _,i in minHeap]

if __name__ == '__main__':
    print("K closest numbers to X are: "  + str(find_closest_elements([5, 6, 7, 8, 9], 3, 7)))
    print("K closest numbers to X are: "  + str(find_closest_elements([2, 4, 5, 6, 9], 3, 6)))
    print("K closest numbers to X are: "  + str(find_closest_elements([2, 4, 5, 6, 9], 3, 10)))

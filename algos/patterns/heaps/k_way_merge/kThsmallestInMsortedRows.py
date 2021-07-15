# Given ‘M’ sorted arrays, find the K’th smallest number among all the arrays.

# Example 1:

# Input: L1=[2, 6, 8], L2=[3, 6, 7], L3=[1, 3, 4], K=5
# Output: 4
# Explanation: The 5th smallest number among all the arrays is 4, this can be verified from the merged 
# list of all the arrays: [1, 2, 3, 3, 4, 6, 6, 7, 8]
# Example 2:

# Input: L1=[5, 8, 9], L2=[1, 7], K=3
# Output: 7
# Explanation: The 3rd smallest number among all the arrays is 7.

from heapq import *

def find_kth_smallest_number(lists, k):
    minHeap = []
    merged = []
    for i,j in enumerate(lists):
        heappush(minHeap, (j[0], i, 0))
    print(minHeap)
    c = 0
    while minHeap:
        r, ln, i = heappop(minHeap)
        c += 1
        if c == k:
            return r
        
        if i + 1 < len(lists[ln]):
            heappush(minHeap, (lists[ln][i+ 1], ln, i + 1))
    return -1

if __name__ == '__main__':
    rv = find_kth_smallest_number([[2,6,8], [3, 6, 7], [1, 3, 4]], 5)
    assert rv == 4
    print("Kth Smallest numbers is " + str(rv))
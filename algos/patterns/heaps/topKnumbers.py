# Given an unsorted array of numbers, find the ‘K’ largest numbers in it.

# Note: For a detailed discussion about different approaches to solve this problem, take a look at Kth Smallest Number.

# Example 1:

# Input: [3, 1, 5, 12, 2, 11], K = 3
# Output: [5, 12, 11]
# Example 2:

# Input: [5, 12, 11, -1, 12], K = 3
# Output: [12, 11, 12]

from heapq import *

def find_k_largest_numbers(nums, k):
    '''
    Time complexity of insertion in MinHeap 3 is log(n) per variable =
    -> Klog(k) + (N-K) log(k) = N Log(N)
    Space = O(k)
    '''
    minHeap = []
    for i in range(k):
        heappush(minHeap, nums[i])

    for i in range(k, len(nums)):
        if nums[i] > minHeap[0]:
            heappop(minHeap)
            heappush(minHeap, nums[i])
    return list(minHeap)

if __name__ == '__main__':
    nums1 = [3, 1, 5, 12, 2, 11]
    k1 = 3
    nums2 = [5, 12, 11, -1, 12]
    k2 = 3
    print(f"Here are the top {k1} numbers " + str(find_k_largest_numbers(nums1, k1)))
    print(f"Here are the top {k2} numbers " + str(find_k_largest_numbers(nums2, k2)))
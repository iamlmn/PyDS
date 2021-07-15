# Problem Statement #
# Given an array of numbers and a number ‘K’, we need to remove ‘K’ numbers from the array such that we are left with maximum distinct numbers.

# Example 1:

# Input: [7, 3, 5, 8, 5, 3, 3], and K=2
# Output: 3
# Explanation: We can remove two occurrences of 3 to be left with 3 distinct numbers [7, 3, 8], we have 
# to skip 5 because it is not distinct and occurred twice. 
# Another solution could be to remove one instance of '5' and '3' each to be left with three 
# distinct numbers [7, 5, 8], in this case, we have to skip 3 because it occurred twice.
# Example 2:

# Input: [3, 5, 12, 11, 12], and K=3
# Output: 2
# Explanation: We can remove one occurrence of 12, after which all numbers will become distinct. Then 
# we can delete any two numbers which will leave us 2 distinct numbers in the result.
# Example 3:

# Input: [1, 2, 3, 3, 3, 3, 4, 4, 5, 5, 5], and K=2
# Output: 3
# Explanation: We can remove one occurrence of '4' to get three distinct numbers.
from collections import Counter
from heapq import *

def find_maximum_distinct_elements(nums, k):
    c = Counter(nums) # O(N) Time & O(N) Space.
    # first find all distinct elements and add counter and add the non distinct to heap
    cnt = 0
    minHeap = []
    for i,j in c.items():
        if j == 1:
            cnt += 1
        else:
            minHeap.append((j, i))
        # make it a heap
        heapify(minHeap)
    while k > 0 and len(minHeap) > 0:
        f,n = heappop(minHeap)
        k -= f - 1

        if k >= 0:
            cnt += 1
    # k removal is not satisfied.
    if k > 0:
        cnt -= k
    return cnt

        

    return -1


if __name__ == '__main__':
    print("Maximum distinct numbers afrer removing k numbers: " + str(find_maximum_distinct_elements([7, 3, 5, 8, 5, 3, 3], 2)))
    print("Maximum distinct numbers afrer removing k numbers: " + str(find_maximum_distinct_elements([3, 5, 12, 11, 12], 3)))
    print("Maximum distinct numbers afrer removing k numbers: " + str(find_maximum_distinct_elements([1, 2, 3, 3, 3, 3, 4, 4, 5, 5,5], 2)))
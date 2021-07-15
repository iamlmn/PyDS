# Given an unsorted array of numbers, find the top ‘K’ frequently occurring numbers in it.

# Example 1:

# Input: [1, 3, 5, 12, 11, 12, 11], K = 2
# Output: [12, 11]
# Explanation: Both '11' and '12' apeared twice.
# Example 2:

# Input: [5, 12, 11, 3, 11], K = 2
# Output: [11, 5] or [11, 12] or [11, 3]
# Explanation: Only '11' appeared twice, all other numbers appeared once.
from heapq import *
def find_k_frequent_numbers(nums, k):
    topNumbersMaxHeap = []
    hmap = dict()
    # count each number frequency
    for i in nums:
        if i not in hmap:
            hmap[i] = 0
        hmap[i] += 1
    for i,j in enumerate(hmap):
        if i < k:
            heappush(topNumbersMaxHeap, (hmap[j], j))
            continue
        if i >= k:
            if hmap[nums[i]] > topNumbersMaxHeap[0][0]:
                heappop(topNumbersMaxHeap)
                heappush(topNumbersMaxHeap, (hmap[j], j))
    return [j for i,j in topNumbersMaxHeap]

def simple_py_version_of_frequent_numbers(nums, k):
    from collections import Counter
    count = Counter(nums)
    return nlargest(k, count, key=count.get)


if __name__ == '__main__':
    print("here are the k frequent numbers : " + str(find_k_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    print("here are the k frequent numbers : " + str(find_k_frequent_numbers([5, 12, 11, 3, 11], 2)))
    print("here are the k frequent numbers : " + str(simple_py_version_of_frequent_numbers([1, 3, 5, 12, 11, 12, 11], 2)))
    print("here are the k frequent numbers : " + str(simple_py_version_of_frequent_numbers([5, 12, 11, 3, 11], 2)))
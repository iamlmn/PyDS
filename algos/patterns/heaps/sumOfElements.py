# Given an array, find the sum of all numbers between the K1’th and K2’th smallest elements of that array.

# Example 1:

# Input: [1, 3, 12, 5, 15, 11], and K1=3, K2=6 
# Output: 23
# Explanation: The 3rd smallest number is 5 and 6th smallest number 15. The sum of numbers coming
# between 5 and 15 is 23 (11+12).
# Example 2:

# Input: [3, 5, 8, 7], and K1=1, K2=4
# Output: 12
# Explanation: The sum of the numbers between the 1st smallest number (3) and the 4th smallest 
# number (8) is 12 (5+7).
from heapq import *
def find_sum_of_elements(nums, k1, k2):
    # find k1 and k2 second smallest numbers first
    s = 0
    minHeap = nums
    heapify(minHeap) # NLog(N)
    for i in range(k1):
        heappop(minHeap)
    
    for i in range(k1 + 1, k2):
        
        s += heappop(minHeap)
        print(s)

    return s


def alternate_solution(nums, k1, k2):
    '''
    Using MinHeap
    Tc: 
    Sc: 
    '''
    maxHeap = []

    for i in range(len(nums)):
        if i < k2 - 1:
            heappush(maxHeap, -nums[i])
        else:
            if -nums[i] > maxHeap[0]:
                heappop(maxHeap)
                heappush(maxHeap, -nums[i])
    
    print(maxHeap)
    s = 0
    for i in range(k2 - k1 - 1):
        s += heappop(maxHeap)

    return s * -1




if __name__ == '__main__':
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(alternate_solution([1, 3, 12, 5, 15, 11], 3, 6)))
    print("Sum of all numbers between k1 and k2 smallest numbers: " + str(alternate_solution([3, 5, 8, 7], 1, 4)))
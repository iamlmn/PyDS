# Given an N * NN∗N matrix where each row and column is sorted in ascending order, find the Kth smallest element in the matrix.

# Example 1:

# Input: Matrix=[
#     [2, 6, 8], 
#     [3, 7, 10],
#     [5, 8, 11]
#   ], 
#   K=5
# Output: 7
# Explanation: The 5th smallest number in the matrix is 7.
from heapq import *
def better_bs_solution(matrix, k):
    pass


def find_kTh_smallest(matrix, k):
    '''
    TC:  O(mn log k)
    SC : O(k)
    '''
    n, c = -1, 0
    minHeap = []
    for i,j in enumerate(matrix):
        heappush(minHeap, (j[0], i, 0))


    while minHeap:
        n, row, i = heappop(minHeap)
        c += 1
        if c == k:
            return n
        if len(matrix[row]) > i + 1:
            heappush(minHeap, (matrix[row][i + 1], row, i + 1)) 
    return n


if __name__ == '__main__':
    print("Kth smallest number is : " + str(find_kTh_smallest([[2,6,8], [3,7,10], [5,8,11]], 5)))



# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.



def myTripleSumZero(array):
    array.sort()
    triplets = []
    for i in range(len(array) - 2):

        left = i + 1
        right = len(array) - 1

        while left < right:
            
            x = [array[i], array[left], array[right]]
            currentSum = sum(x)
            if currentSum == 0 and x not in triplets: 
                triplets.append(x) 
                left += 1
                right -= 1
            elif currentSum < 0:
                left += 1
            elif currentSum > 0:
                right -= 1


    return triplets


if __name__ == '__main__':
    nums1 = [-3, 0, 1, 2, -1, 1, -2]
    x1 = myTripleSumZero(nums1)
    print(x1)
    assert x1 == [[-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]]
    nums2 = [-5, 2, -1, -2, 3]
    x2 = myTripleSumZero(nums2)
    print(x2)
    assert x2 == [[-5, 2, 3], [-2, -1, 3]]



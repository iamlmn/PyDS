# Given an array of unsorted numbers, find all unique triplets in it that add up to zero.

# Example 1:

# Input: [-3, 0, 1, 2, -1, 1, -2]
# Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
# Explanation: There are four unique triplets whose sum is equal to zero.
# Example 2:

# Input: [-5, 2, -1, -2, 3]
# Output: [[-5, 2, 3], [-2, -1, 3]]
# Explanation: There are two unique triplets whose sum is equal to zero.


def search_pair(array, targetSum, left, triplets):
    right = len(array) - 1

    while left < right:
        currentSum = array[left] + array[right]

        if currentSum == targetSum:
            triplets.append([-targetSum, array[left], array[right]])
            left += 1
            right -= 1

            while left < right and array[left] == array[left - 1]:
                left += 1

            while left < right and array[right] == array[right + 1]:
                right -= 1
        elif targetSum > currentSum:
            left += 1

        else:
            right -= 1


            
def myTripleSumZero(array):
    array.sort()
    triplets = []
    
    for i in range( len(array)):
        if i > 0 and array[i] == array[i - 1]:
            continue
        search_pair(array, -array[i], i + 1, triplets)

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



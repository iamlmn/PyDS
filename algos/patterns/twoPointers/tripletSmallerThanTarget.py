# Given an array arr of unsorted numbers and a target sum, count all triplets in it such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three different indices. Write a function to return the count of such triplets.

# Example 1:

# Input: [-1, 0, 2, 3], target=3 
# Output: 2
# Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]
# Example 2:

# Input: [-1, 4, 2, 1, 3], target=5 
# Output: 4
# Explanation: There are four triplets whose sum is less than the target: 
#    [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]


def countSmallerThanTarget(array, target):
    triplets = []

    array.sort()

    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left < right:
            x = [array[i], array[left], array[right]]
            currentSum = sum(x)
            if currentSum < target:
                for j in range(right, left, -1):
                    triplets.append([array[i], array[left], array[j]])
                left += 1
            else:
                right -= 1


    return len(triplets)


if __name__ == '__main__':
    nums1 = [-1, 0, 2, 3]
    target1 = 3

    x1 = countSmallerThanTarget(nums1, target1)
    print(x1)


    x2 = countSmallerThanTarget([-1, 4, 2, 1, 3], 5)
    print(x2)



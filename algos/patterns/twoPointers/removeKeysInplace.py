# Given an unsorted array of numbers and a target ‘key’, 
# remove all instances of ‘key’ in-place and return the new length of the array.

# Example 1:

# Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
# Output: 4
# Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
# Example 2:

# Input: [2, 11, 2, 2, 1], Key=2
# Output: 2
# # Explanation: The first two elements after removing every 'Key' will be [11, 1].


def removeKey(nums, key):
    # i = 1
    nexti = 0

    for i in range(len(nums)):
        if nums[nexti] != key:
            nums[nexti] = nums[i]
            nexti += 1 
    return nexti 


if __name__ == '__main__':
    nums1 = [3, 2, 3, 6, 3, 10, 9, 3]
    x1 = removeKey(nums1, 3)
    # assert x1 == 4
    print(f"{x1}")
# Given an array of sorted numbers, remove all duplicates from it. 
# You should not use any extra space; after removing the duplicates in-place return the new length of the array.

# Example 1:

# Input: [2, 3, 3, 3, 6, 9, 9]
# Output: 4
# Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
# Example 2:

# Input: [2, 2, 2, 11]
# Output: 2
# Explanation: The first two elements after removing the duplicates will be [2, 11].


def removeDuplicates(nums):
    nexti = 1

    for i in range(1, len(nums)):
        if nums[nexti- 1] != nums[i]:
            nums[nexti] = nums[i]
            nexti += 1
    

    return nexti
if __name__ == '__main__':
    nums1 = [2, 3, 3, 3, 6, 9, 9]
    nums2 = [2, 2, 2, 11]

    print(f"{removeDuplicates(nums1)}")
    print(f"{removeDuplicates(nums2)}")

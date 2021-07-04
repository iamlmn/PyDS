# Given a set of distinct numbers, find all of its permutations.

# Permutation is defined as the re-arranging of the elements of the set. For example, {1, 2, 3} has the following six permutations:

# {1, 2, 3}
# {1, 3, 2}
# {2, 1, 3}
# {2, 3, 1}
# {3, 1, 2}
# {3, 2, 1}
# If a set has ‘n’ distinct elements it will have n!n! permutations.

# Example 1:

# Input: [1,3,5]
# Output: [1,3,5], [1,5,3], [3,1,5], [3,5,1], [5,1,3], [5,3,1]

from collections import deque
def find_permutations_iterative(nums):
    numslength = len(nums)
    result = []
    permutations = deque()
    permutations.append([])

    for i in nums:
        n = len(permutations)
        for _ in range(n):
            oldPermutation = permutations.popleft()
            # create new permutations.
            for j in range(len(oldPermutation) + 1):
                newPermutation = list(oldPermutation)
                newPermutation.insert(j, i)
                if len(newPermutation) == numslength:
                    result.append(newPermutation)
                else:
                    permutations.append(newPermutation)
    return result


def find_permuations_recursively(nums, idx=0,  oldPermutation=[], result=[]):

    if len(nums) == idx:
        result.append(oldPermutation)

    else:
        for i in range(len(oldPermutation) + 1):
            newPermutation = list(oldPermutation)
            newPermutation.insert(i, nums[idx])
            find_permuations_recursively(nums, idx + 1, newPermutation, result)

    

if __name__ == '__main__':
    arr1 = [1, 3, 5]
    r1 = find_permutations_iterative(arr1)
    print(r1)
    assert r1 == [[5, 3, 1], [3, 5, 1], [3, 1, 5], [5, 1, 3], [1, 5, 3], [1, 3, 5]] 

    # recursive
    r12 = []
    find_permuations_recursively(arr1, 0, [], r12)
    print("recursive output: ", r12)
    assert r1 == r12
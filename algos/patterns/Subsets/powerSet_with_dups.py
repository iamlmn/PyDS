# Given a set of numbers that might contain duplicates, find all of its distinct subsets.

# Example 1:

# Input: [1, 3, 3]
# Output: [], [1], [3], [1,3], [3,3], [1,3,3]
# Example 2:

# Input: [1, 5, 3, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3], [3,3], [1,3,3], [3,3,5], [1,5,3,3] 


def find_subsets(nums):
    nums.sort()
    # visited = set()
    subsets = [[]]
    for i in range(len(nums)):
        for j in range(len(subsets)):
            
            
    return subsets

def find_subsets_recursively(nums):
    pass


if __name__ == '__main__':
    arr1 = [1, 3, 3]
    arr2 = [1, 5, 3, 3]

    r1 = find_subsets(arr1)
    r2 = find_subsets(arr2)
    print(r1)
    print(r2)

    assert r1 == 
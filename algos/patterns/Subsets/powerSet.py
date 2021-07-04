# Given a set with distinct elements, find all of its distinct subsets.

# Example 1:

# Input: [1, 3]
# Output: [], [1], [3], [1,3]
# Example 2:

# Input: [1, 5, 3]
# Output: [], [1], [5], [3], [1,5], [1,3], [5,3], [1,5,3]


def find_subsets(nums):
    subsets = []

    subsets.append([])

    for i in nums:
        for j in range(len(subsets)):
            subsets.append(subsets[j] + [i])

    return subsets

def find_subsets_recursively(nums, idx = None):
    if idx is None:
        idx = len(nums) - 1
    if idx < 0:
        return [[]]

    ele = nums[idx]
    subsets = find_subsets_recursively(nums, idx - 1)

    for i in range(len(subsets)):
        currentSubset = subsets[i]
        subsets.append(currentSubset + [ele])
    return subsets

# using bit manipulation
def find_subsets_using_bits(nums):
    subsets = []
    n = len(nums)
    start = 2 ** n
    end = 2 ** (n + 1)
    print("start, end = ",start , end)
    for i in range(start, end):
        bitmask = bin(i)[3:]
        subsets.append([nums[j] for j in range(n) if bitmask[j] == '1'])
    return subsets
   

if __name__ == '__main__':
    arr1 = [1, 3]
    arr2 = [1, 5, 3]

    r1 = find_subsets(arr1)
    r2 = find_subsets(arr2)
    print(r1)
    print(r2)
    r12 = find_subsets_recursively(arr1)
    r22 = find_subsets_recursively(arr2)

    print(r12)
    print(r22)

    # using bit manipulation
    
    r13 = find_subsets_using_bits(arr1)
    r23 = find_subsets_using_bits(arr2)
    print(r13)
    print(r23)
    
    assert r1 == [[], [1], [3], [1, 3]]
    assert r2 == [[], [1], [5], [1, 5], [3], [1, 3], [5, 3], [1, 5, 3]]
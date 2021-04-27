# Given an array of unsorted numbers and a target number, 
# find all unique quadruplets in it, whose sum is equal to the target number.

# Example 1:

# Input: [4, 1, 2, -1, 1, -3], target=1
# Output: [-3, -1, 1, 4], [-3, 1, 1, 2]
# Explanation: Both the quadruplets add up to the target.
# Example 2:

# Input: [2, 0, -1, 1, -2, 2], target=2
# Output: [-2, 0, 2, 2], [-1, 0, 1, 2]
# Explanation: Both the quadruplets add up to the target.

def getQuads(array, target):
    quads = []
    array.sort()
    for i in range(len(array) - 2):
        left = i + 1
        right = len(array) - 1

        while left<= right:

            fourthNum = target - (array[i] + array[left] + array[right] )
            # print(fourthNum)
            for j in range(left + 1, right):
                if array[j]  == fourthNum:
                    quads.append([array[i], array[left], array[j], array[right]])
                    break

            if fourthNum < 0:
                right -= 1
            else:
                left += 1

    return quads


if __name__ == '__main__':
    num1 = [4, 1, 2, -1, 1, -3]
    target1 = 1
    x1 = getQuads(num1, target1)
    assert x1 ==  [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    print(x1)
    
    num2 = [2, 0, -1, 1, -2, 2]
    target2 = 2
    x2 = getQuads(num2, target2)
    assert x2 == [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    print(x2)
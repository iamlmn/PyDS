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

# def getQuads(array, target):
#     quads = []
#     array.sort()
#     for i in range(len(array) - 2):
#         left = i + 1
#         right = len(array) - 1

#         while left<= right:

#             fourthNum = target - (array[i] + array[left] + array[right] )
#             # print(fourthNum)
#             for j in range(left + 1, right):
#                 if array[j]  == fourthNum:
#                     quads.append([array[i], array[left], array[j], array[right]])
#                     break

#             if fourthNum < 0:
#                 right -= 1
#             else:
#                 left += 1

#     return quads


def getQuads(array, target):
    array.sort()
    quads = []
    for i in range(len(array) - 3):
        if i > 0 and array[i] == array[i - 1]:
            continue
        
        for j in range(i+1, len(array) - 2):
            if j > i+1 and array[j] == array[j - 1]:
                continue
            
            search_pair(array, i, j, j + 1, target, quads)
    return quads

def search_pair(array, x, y, left, target, quads):
    right = len(array) - 1

    while left < right:
        currentSum = array[x] + array[y] + array[left] + array[right]

        if currentSum == target:
            quads.append([array[x], array[y], array[left], array[right]])
            left += 1
            right -= 1

            while left < right and array[left] == array[left - 1]:
                left += 1
            
            while left < right and array[right] == array[right - 1]:
                right -= 1

        elif currentSum < target:
            left += 1

        else:
            right -= 1




if __name__ == '__main__':
    num1 = [4, 1, 2, -1, 1, -3]
    target1 = 1
    x1 = getQuads(num1, target1)
    print(x1)
    assert x1 ==  [[-3, -1, 1, 4], [-3, 1, 1, 2]]
    

    num2 = [2, 0, -1, 1, -2, 2]
    target2 = 2
    x2 = getQuads(num2, target2)
    print(x2)
    assert x2 == [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    


    num3 = [7, 6, 4, -1, 1, 2]
    target3 = 16
    x3 = getQuads(num3, target3)
    # assert x2 == [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    print(x3)

    

    num4 = [1, 2, 3, 4, 5, 6, 7]
    target4 = 10
    x4 = getQuads(num4, target4)
    # assert x2 == [[-2, 0, 2, 2], [-1, 0, 1, 2]]
    print(x4)
    
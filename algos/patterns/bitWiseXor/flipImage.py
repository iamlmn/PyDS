# Given a binary matrix representing an image, we want to flip the image horizontally, then invert it.

# To flip an image horizontally means that each row of the image is reversed. For example, flipping [0, 1, 1] horizontally results in [1, 1, 0].

# To invert an image means that each 0 is replaced by 1, and each 1 is replaced by 0. For example, inverting [1, 1, 0] results in [0, 0, 1].

# Example 1:

# Input: [
#   [1,0,1],
#   [1,1,1],
#   [0,1,1]
# ]
# Output: [
#   [0,1,0],
#   [0,0,0],
#   [0,0,1]
# ]
# Explanation: First reverse each row: [[1,0,1],[1,1,1],[1,1,0]]. Then, invert the image: [[0,1,0],[0,0,0],[0,0,1]]

# Example 2:

# Input: [
#   [1,1,0,0],
#   [1,0,0,1],
#   [0,1,1,1], 
#   [1,0,1,0]
# ]
# Output: [
#   [1,1,0,0],
#   [0,1,1,0],
#   [0,0,0,1],
#   [1,0,1,0]
# ]
# Explanation: First reverse each row: [[0,0,1,1],[1,0,0,1],[1,1,1,0],[0,1,0,1]]. Then invert the image: [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]



def getFlipInvertedImage(arr):
    '''
    Time : O(m * n)
    Space : O(N)

    '''
    newArray = []
    # get column count
    bit_c = len(arr[0])
    print(bit_c)
    # flip row
    d = [1 for i in range(bit_c)]


    for i in range(len(arr)):

        newArray.append([(j ^ 1) for j in arr[i][::-1]])

    return newArray


if __name__ == '__main__':
    arr1 = [[1,0,1],[1,1,1],[0,1,1]]
    arr2 = [
  [1,1,0,0],
  [1,0,0,1],
  [0,1,1,1], 
  [1,0,1,0]
]


    r1 = getFlipInvertedImage(arr1)
    r2 = getFlipInvertedImage(arr2)


    print(r1)
    print(r2)

    assert r1 == [[0,1,0],[0,0,0],[0,0,1]]
    assert r2 == [[1,1,0,0],[0,1,1,0],[0,0,0,1],[1,0,1,0]]
# Given an array of characters where each character represents a fruit tree, 
# you are given two baskets and your goal is to put maximum number of fruits in each basket. 
# The only restriction is that each basket can have only one type of fruit.

# You can start with any tree, but once you have started you can’t skip a tree. 
# You will pick one fruit from each tree until you cannot, i.e., 
# you will stop when you have to pick from a third fruit type.

# Write a function to return the maximum number of fruits in both the baskets.

'''
Input: Fruit=['A', 'B', 'C', 'A', 'C']
Output: 3
Explanation: We can put 2 'C' in one basket and one 'A' in the other from the subarray ['C', 'A', 'C']

Input: Fruit=['A', 'B', 'C', 'B', 'B', 'C']
Output: 5
Explanation: We can put 3 'B' in one basket and two 'C' in the other basket. 
This can be done if we start with the second letter: ['B', 'C', 'B', 'B', 'C']
'''


def getMaxFruits(array):
    '''
    TC : O(N)
    SC: O(N)
    '''

    maxFruits = 0
    fruitFrequency = {}
    start = 0

    for i in range(len(array)):
        cFruit = array[i]
        if cFruit not in fruitFrequency:
            fruitFrequency[cFruit] = 0
        fruitFrequency[cFruit] += 1

        while len(fruitFrequency) > 2:
            rFruit = array[start]
            fruitFrequency[rFruit] -= 1
            if fruitFrequency[rFruit] == 0:
                del fruitFrequency[rFruit]
            start += 1

        maxFruits = max(maxFruits, i - start + 1)
    return maxFruits


if __name__ == '__main__':

    fruit1 = ['A', 'B', 'C', 'A', 'C']
    fruit2 = ['A', 'B', 'C', 'B', 'B', 'C']

    print(f" Max fruits from {fruit1} are {getMaxFruits(fruit1)} ")
    print(f" Max fruits from {fruit2} are {getMaxFruits(fruit2)} ")
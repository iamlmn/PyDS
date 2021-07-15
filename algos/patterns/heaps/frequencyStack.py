# Frequency Stack (hard) #
# Design a class that simulates a Stack data structure, implementing the following two operations:

# push(int num): Pushes the number ‘num’ on the stack.
# pop(): Returns the most frequent number in the stack. If there is a tie, return the number which was pushed later.
# Example:

# After following push operations: push(1), push(2), push(3), push(2), push(1), push(2), push(5)
 
# 1. pop() should return 2, as it is the most frequent number
# 2. Next pop() should return 1
# 3. Next pop() should return 2

from heapq import *
class FrequencyStack:
    def __init__(self):
        self.stack = []
        self.freqStack = []
    def push(self, num):
        self.stack.append(num)
        heappush(self.freqStack, )
        return 0

    def pop(self):
        c = -1
        if self.freqStack:
            f,c = heappop(self.freqStack)
            if f + 1 < 0:
                heappush(self.stack())
        return c

if __name__ == '__main__':
    frequencyStack = FrequencyStack()
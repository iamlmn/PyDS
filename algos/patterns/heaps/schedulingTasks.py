# Scheduling Tasks (hard) #
# You are given a list of tasks that need to be run, in any order, on a server. Each task will take one CPU interval to execute but once a task has finished, it has a cooling period during which it can’t be run again. If the cooling period for all tasks is ‘K’ intervals, find the minimum number of CPU intervals that the server needs to finish all tasks.

# If at any time the server can’t execute any task then it must stay idle.

# Example 1:

# Input: [a, a, a, b, c, c], K=2
# Output: 7
# Explanation: a -> c -> b -> a -> c -> idle -> a
# Example 2:

# Input: [a, b, a], K=3
# Output: 5
# Explanation: a -> b -> idle -> idle -> a
from collections import Counter, deque
from heapq import *

def schedule_tasks(tasks, k):
    '''
    '''
    intervalCount = 0
    c = Counter(tasks) # O(N)
    maxHeap = []
    # O(NLogN)
    for e,v in c.items(): 
        heappush(maxHeap, (-v, e)) 

    # Now the loop
    res = []
    idle = 0
    # tempList = []
    while maxHeap:
        it = k + 1
        tempList = []
        while it > 0 and maxHeap:
            f, c = heappop(maxHeap)
            res.append(c)
            intervalCount += 1
            if f + 1 < 0:
                tempList.append((f+1, c))
            it -= 1
   

        for f,c in tempList:
            heappush(maxHeap, (f,c))

        if maxHeap:
            intervalCount += it
        

        

        
    return intervalCount

if __name__ == '__main__':
    print("Minimum interval needed to execute all tasks. " + str(schedule_tasks(['a', 'a', 'a', 'b', 'c', 'c'], 2)))
    print("Minimum interval needed to execute all tasks. " + str(schedule_tasks(['a', 'b', 'a'], 3)))
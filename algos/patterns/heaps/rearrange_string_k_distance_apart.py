# Rearrange String K Distance Apart (hard) #
# Given a string and a number ‘K’, find if the string can be rearranged such that the same characters are at least ‘K’ distance apart from each other.

# Example 1:

# Input: "mmpp", K=2
# Output: "mpmp" or "pmpm"
# Explanation: All same characters are 2 distance apart.
# Example 2:

# Input: "Programming", K=3
# Output: "rgmPrgmiano" or "gmringmrPoa" or "gmrPagimnor" and a few more
# Explanation: All same characters are 3 distance apart.
# Example 3:

# Input: "aab", K=2
# Output: "aba"
# Explanation: All same characters are 2 distance apart.
# Example 4:

# Input: "aappa", K=3
# Output: ""
# Explanation: We cannot find an arrangement of the string where any two 'a' are 3 distance apart.
from collections import deque
from heapq import *
from collections import Counter
def reOrganizeString(s, k):
    cs = Counter(s)
    res = ""
    maxHeap = []
    # create a max Heap
    for i,v in cs.items():
        heappush(maxHeap, (-v,str(i)))

    q = deque()
    
    while maxHeap:
        f, c = heappop(maxHeap)
        res = res + c

        q.append((f + 1,c))
        print(q)
        if len(q) == k:
            f,c = q.popleft()
            if -f > 0:
                heappush(maxHeap, (f, c))
    return res
    if len(res) == len(s):
        return res

    return ""

if __name__ == '__main__':
    print("Reorganizing string: " + reOrganizeString("mmpm", 2))
    print("Reorganizing string: " + reOrganizeString("Programming", 3))
    print("Reorganizing string: " + reOrganizeString("aab", 2))
    print("Reorganizing string: " + reOrganizeString("aaabcc", 2))


    # https://leetcode.com/discuss/general-discussion/1127238/master-heap-by-solving-23-questions-in-4-patterns-category
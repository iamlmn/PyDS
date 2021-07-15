# Problem Statement #
# Given a string, find if its letters can be rearranged in 
# such a way that no two same characters come next to each other.

# Example 1:

# Input: "aappp"
# Output: "papap"
# Explanation: In "papap", none of the repeating characters come next to each other.
# Example 2:

# Input: "Programming"
# Output: "rgmrgmPiano" or "gmringmrPoa" or "gmrPagimnor", etc.
# Explanation: None of the repeating characters come next to each other.
# Example 3:

# Input: "aapa"
# Output: ""
# Explanation: In all arrangements of "aapa", atleast two 'a' will come together e.g., "apaa", "paaa".

from heapq import *
from collections import Counter
def rearrange_string(stri):
    c = Counter(stri)
    result = ""
    maxHeap = []
    # create a max Heap
    for k,v in c.items():
        heappush(maxHeap, (-v,str(k)))
    pf, pc = 0, None
    
    while maxHeap:
        print(pc)
        f, c = heappop(maxHeap)
        
        if pc and pf < 0:
            print("Pushing", pf, pc, maxHeap)
            heappush(maxHeap, (pf,pc))        
        result = result + str(c)
        pc = c
        pf = f + 1

    return result

if __name__ == '__main__':
    print("Rearranged string: " + rearrange_string("aappp"))
    print("Rearranged string: " + rearrange_string("Programming"))
    print("Rearranged string: " + rearrange_string("apppb"))
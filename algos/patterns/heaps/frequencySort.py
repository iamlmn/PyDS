# Given a string, sort it based on the decreasing frequency of its characters.

# Example 1:

# Input: "Programming"
# Output: "rrggmmPiano"
# Explanation: 'r', 'g', and 'm' appeared twice, so they need to appear before any other character.
# Example 2:

# Input: "abcbab"
# Output: "bbbaac"
# Explanation: 'b' appeared three times, 'a' appeared twice, and 'c' appeared only once.
from heapq import *
from collections import Counter
def sort_character_by_frequency(str):
    minHeap = []
    c = Counter(str)

    for i,j in c.items():
        heappush(minHeap, (j, i))
    res = ""

    while len(minHeap):
       c, n = heappop(minHeap)
       while c:
           res = n + res
           c -= 1

    return res

if __name__ == '__main__':
    print("String after sorting characters by frequency: " + sort_character_by_frequency("Programming"))
    print("String after sorting characters by frequency: " + sort_character_by_frequency("abcbab"))
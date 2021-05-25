# Given two lists of intervals, find the intersection of these two lists. Each list consists of disjoint intervals sorted on their start time.

# Example 1:

# Input: arr1=[[1, 3], [5, 6], [7, 9]], arr2=[[2, 3], [5, 7]]
# Output: [2, 3], [5, 6], [7, 7]
# Explanation: The output list contains the common intervals between the two lists.
# Example 2:

# Input: arr1=[[1, 3], [5, 7], [9, 12]], arr2=[[5, 10]]
# Output: [5, 7], [9, 10]
# Explanation: The output list contains the common intervals between the two lists.


def merge(a, b):
    result = []

    i = 0 
    j = 0

    while i <= len(a) - 1 and j <= len(b) - 1:
        if (b[j][0] >= a[i][0] and b[j][0] <= a[i][1])   or (a[i][0] >= b[j][0] and a[i][0] <= b[j][1]):
            start = max(a[i][0], b[j][0])
            end = min(a[i][1], b[j][1])
            result.append([start, end])

        if a[i][1] < b[j][1]:
            i += 1
        else:
            j += 1


    return result


if __name__ == '__main__':
    print("Intervals intersection: " + str(merge([[1,3], [5,6] , [7,9]], [[2,3], [5,7]] )))
    print("Intervals intersection: " + str(merge([[1,3], [5,7] , [9,12]], [[5,10]] )))
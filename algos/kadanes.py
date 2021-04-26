# find the longest continuous subarray with maximum sum.


def kadane(array):
    '''

    '''
    maxSofar = array[0]
    maxEndingHere = array[0]
    start = 0
    end = 0
    for i in array[1:]:
        if i > maxEndingHere + i:
            start = array.index(i)

        maxEndingHere = max(maxEndingHere + i, i)
        
        if maxSofar > maxEndingHere:
            end = array.index(i)
        maxSofar = max(maxSofar, maxEndingHere)

    return maxSofar, start, end

if __name__ == '__main__':
    ar = [3, 5, -9, 1, 3, -2, 3, 4, 7, 2, -9, 6, 3, 1, -5, 4]
    print(f"Max array : {kadane(ar)}")
# Given an array, find the average of all contiguous subarrays of size ‘K’ in it.

# Array: [1, 3, 2, 6, -1, 4, 1, 8, 2], K=5

def bruteForce5numAvg(array, size = 5):
    
    # Time Complexity = O(N * K), Space O(N/k)
    i = 0
    avg = []
    while (i + size - 1 < len(array)):
        avg.append(sum(array[i:i+size])/ size)
        i += 1
    return avg


def SlidingWindow(array, size =5):
    avg = []
    windowSum = 0
    windowStart = 0
    windowEnd = 0
    for i in range(len(array)):
        windowSum += array[i]

        if i >= size - 1:
            avg.append(windowSum/size)
            windowSum -= array[windowStart]
            windowStart += 1
    return avg


if __name__ == '__main__':
    array = [1, 3, 2, 6, -1, 4, 1, 8, 2]
    print(f" 5 window Average of {array} is {bruteForce5numAvg(array, size = 5)}")
    print(f"With sliding window in Time complexity of O(N) {SlidingWindow(array, size =5)}")
    
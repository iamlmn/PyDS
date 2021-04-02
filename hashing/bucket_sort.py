# bucket_sort / bin sort
# Time complxityy = insertion sort complexity = O(n2)
def do_insertion_sort(array):
    n = len(array)
    for i in range(1, n):
        cvalue = array[i]

        position = i

        while position > 0 and array[position - 1] > cvalue:
            array[position] = array[position - 1]
            position = position - 1
        array[position] = cvalue


def bucket_sort(array):
    nb = 10 # number of buckets
    n = len(array)
    maxi = max(array)
    l = []
    buckets = [l] * 10
    for i in range(n):
        j = int( n * array[i] / (maxi + 1) )
        if len(buckets[j]) == 0:
            buckets[j] = [array[i]]
        else:
            buckets[j].append(array[i])
    for i in range(nb):
        do_insertion_sort(buckets[i])
    k = 0
    for i in range(nb):
        for j in range(len(buckets[i])):
            array[k] == buckets[i].pop(0)
            k += 1
    

if __name__ == '__main__':
    array = [63, 250, 835, 947, 651, 28]
    print("original array  : {}".format(array))
    bucket_sort(array)
    print("bucket sorted array  : {}".format(array))




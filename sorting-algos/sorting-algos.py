from tqdm import tqdm

def do_selection_sort(array, order_type='asc'):
    '''
    Sort inplace by finding the min in a given array 
    and assigning it to the position starting 
    from begining or end based on asc or desc.

    Selection Sort
    - Unstable sort.
        - Time complexity = O(n*n-1) = O(n2)
        - Space Complexity = O(1)
        - O(n) Swaps - Only sort to have this O(n) swappings.

    Params:
        array : List of numbers
        order_type: 'asc' for Ascending / desc for Descending.
    '''
    # sorted_array = []
    # for i in tqdm(range(0, len(array))): 
    #     if sorted_array == []:
    #         sorted_array = [min(array)]
    #     else:
    #         sorted_array.append(min(array))  # n * O(n)
    #     array.pop(i)

    # return sorted_array

    n = len(array)
    for i in range(n):
        position = i
        for j in range(i+1, n):
            if order_type == 'desc':
                if array[j] > array[position]:
                    position = j
            else:
                if array[j] < array[position]:
                    position = j

        temp = array[i]
        array[i] = array[position]
        array[position] = temp


def do_insertion_sort(array, order_type='asc'):
    '''
    Checks if the left position element is in correct 
    order if not traverse back till it is in correct order.
    Sorts the array inplace.
    
    Stable Sorting Algorithm
        - Time complexity = O(n*n-1) = O(n2)
        - O(n2) Swappings.

    If the array is already sorted : 
     it will make only O(1) swaps and O(n) Time complexity


    Params:
        array : List of numbers
        order_type: 'asc' for Ascending / desc for Descending.
    '''


    n = len(array)      
    for i in range(1, n):
        cvalue = array[i]
        position = i 
        while position > 0 and ((order_type == 'asc' and (array[position-1] > cvalue)) or (order_type == 'desc' and (array[position-1] < cvalue))):
            array[position] = array[position - 1]
            position = position - 1
        array[position] = cvalue 



def do_bubble_sort(array, order_type='asc'):
    '''
    Checks if the left position element is in correct 
    order if not traverse back till it is in correct order.
    
    Stable Sorting Algorithm
        - Time complexity = O(n*n-1) = O(n2)
        - O(n2) Swappings.
        - Space complexity - O(1)

    If the array is already sorted : 
     it will make only O(1) swaps and O(n2) Time complexity
    '''                
    n = len(array)
    swap = 0
    for _pass in range(n - 1, 0, -1):
        for i in range(_pass):   
            if array[i] > array[i+1] and order_type == 'asc':
                temp = array[i]
                array[i] = array[i+1]
                array[i + 1] = temp
                swap = 1

            if array[i] < array[i+1] and order_type == 'desc':
                temp = array[i]
                array[i] = array[i+1]
                array[i + 1] = temp
                swap = 1
        if swap == 0:
            print("No SWAPs done, hence exiting loop with time O(n-1)")

def do_shell_sort(array, order_type='asc'):
    '''
    Select an element and compare after a gap. 
    Similar to insertion sort, insert selected element at the gap.
    
    Stable Sorting Algorithm
        - Time complexity = O(n*n-1) = O(n2)
        - O(n2) Swappings.
        - Space complexity - O(1)

    If the array is already sorted : 
     it will make only O(1) swaps and O(n2) Time complexity
    '''                
    n = len(array)
    gap = n//2
    while gap > 0:
        i = gap
        while i < n :
            temp = array [i]
            j = i - gap
            while j>= 0 and ((array[j] > temp) and order_type == 'asc' ) or ((array[j] < temp) and  order_type == 'desc') :
                array[j + gap] = array[j]
                j= j - gap
            array[j + gap]  = temp
            i = i + 1
        gap = gap // 2  






## Merge sort

def do_mergesort(array, left, right, order_type = 'asc'):
    ''' 
    '''

    # if order_type == 'asc':
    if (left < right) :
        mid = (left + right) // 2
        do_mergesort(array, left, mid, order_type=order_type)
        do_mergesort(array, mid + 1, right, order_type=order_type)
        # print("Merging ")
        merge(array, left, mid, right, order_type=order_type)
    # else:
    #     raise RuntimeError("Invalid Scenario check the if statement")

def merge(array, left, mid, right,order_type):
    i = left
    j = mid + 1
    k = left
    barray = [0] * (right + 1) 
    while i <= mid and j <= right:

        if order_type == 'asc' and array[i] < array[j]:
            barray[k] = array[i]
            i = i + 1
        elif order_type == 'desc' and array[i] > array[j]:
            barray[k] = array[i]
            i = i + 1
        else:
            barray[k] = array[j]
            j = j + 1
        k = k + 1

    while i <= mid:
        # if array[i] <= array[j]:
        barray[k] = array[i]
        i = i + 1
        k  = k + 1

    while j <= right:
        # if array[i] <= array[j]:
        barray[k] = array[j]
        j = j + 1
        k = k + 1

    assert k == right + 1
    # print("Copying", barray)
    for x in range(left, right + 1):
        array[x] = barray[x]

    # print(barray)

## Quick sort.

def partition(array, low, high, order_type):
    i = low + 1
    j = high
    pivot = array[low]

    while True:

        if order_type == 'desc':
            while i <= j and array[i] >= pivot:
                i += 1
            while i <= j and array[j] < pivot:
                j=j - 1
        else:
            while i <= j and array[i] <= pivot:
                i += 1
            while i <= j and array[j] > pivot:
                j=j - 1            

        if i <= j:
            array[i], array[j] = array[j], array[i]
        else:
            break
    array[low], array[j] = array[j], array[low]
    return j # new pivot


def do_quicksort(array, low, high, order_type='asc'):
    if low < high:
        pi = partition(array, low, high, order_type=order_type)
        do_quicksort(array, low, pi - 1)
        do_quicksort(array, pi + 1, high)

        
    



if __name__ == '__main__':
    # Playing with Selection sort.
    print("\n ************ Selection Sort *************")
    array = [1 , 54, 23, 53, 12, 5]
    print(f'Original array {array}')
    do_selection_sort(array)
    print(f'After asc selection sort : {array}')
    do_selection_sort(array, order_type='desc')
    print(f'After desc selection sort : {array}')


    # Playing with Insertion sort.
    array = [1 , 54, 23, 53, 12, 5]
    print("\n ************ Insertion Sort *************")
    print(f'Original array {array}')
    do_insertion_sort(array)
    print(f'After asc insertion sort : {array}')
    do_insertion_sort(array, order_type='desc')
    print(f'After desc insertion sort : {array}')


    # Playing with Bubble sort.
    array = [1 , 54, 23, 53, 12, 5]
    print("\n ************ Bubble Sort *************")
    print(f'Original array {array}')
    do_bubble_sort(array)
    print(f'After asc bubble sort : {array}')
    do_bubble_sort(array, order_type='desc')
    print(f'After desc bubble sort : {array}')


    # Playing with Shell sort.
    array = [1 , 54, 23, 53, 12, 5]
    print("\n ************ Shell Sort *************")
    print(f'Original array {array}')
    do_bubble_sort(array)
    print(f'After asc shell sort : {array}')
    do_bubble_sort(array, order_type='desc')
    print(f'After desc shell sort : {array}')


    # Playing with Merge sort.
    array = [1 , 54, 23, 53, 12, 5]
    print("\n ************ Merge Sort *************")
    print(f'Original array {array}')
    do_mergesort(array, 0, len(array)- 1)
    print(f'After asc merge sort : {array}')
    do_mergesort(array, 0, len(array)- 1, order_type='desc')
    print(f'After desc merge sort : {array}')


    # Playing with quick sort
    array = [1 , 54, 23, 53, 12, 5]
    print("\n ************ Quick Sort *************")
    print("Unstable sorting")
    print("Complexity : Time : n log(n) \n Space : o(n log (n)")
    print(f'Original array {array}')
    do_quicksort(array, 0, len(array) - 1)
    print(f'After asc quick sort : {array}')
    do_quicksort(array, 0, len(array)- 1, order_type='desc')
    print(f'After desc merge sort : {array}')




# Sorting Algorithms in Python

Index based sort :
1. Count Sort
2. Bucket Sort
3. Radix Sort

Result all are comparison based sorting.

1. Selection Sort
    - Unstable sort.
        - Time complexity = O(n*n-1) = O(n2)
        - Space Complexity = O(1)
        - O(n) Swaps - Only sort to have this O(n) swappings.
    Even if the array is sorted takes the same complexity.

2.  Insertion Sort 
    - Stable sorting algorithm.
        - Time complexity = O(n*n-1) = O(n2)
        - Space Complexity = O(1)
        - O(n2) Swappings.

        Works better than selection sort when the array is sorted.

3. Bubble Sort  
    - Stable sorting algorithm.
        - Time complexity = O(n*n-1) = O(n2)
        - Space Complexity = O(1)
        - O(n2) Swappings.

4. Shell Sort
    - Select an element and compare after a gap. Similar to insertion sort, insert selected element at the gap.
    Gap can be any prime number less than the length of array, generally its 2.

    - Unstable sorting algorithm.
        - Time complexity = O(n log(n) ^ 2)
        - Space Complexity = O(1)
        - swapping depends on gap

    Why? Its an adaptive sorting algorithm and works faster on partially sorted arrays.
    When?

5. Merge Sort
    - Stable sorting algorithm.
        - Time complexity = O(n*n-1) = O(n log(n))
        - Space Complexity = O(n)

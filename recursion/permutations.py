# Time & Space complexity : o(n * n!)
# The algo swaps the value throu iterations and recursively arranges it for all possibilities & swaps back to the original.
def permutaiton(array):
    permutations = []
    permutationHelper(0, array, permutations)
    return permutations

def permutationHelper(i, array, permutations):
    if i == len(array) - 1:
        # print(i, array[:])
        permutations.append(array[:])
    else:
        for j in range(i , len(array)):
            # print(f"Array before swapping : {array}")
            swap(array, i , j)
            # print(f"calling permutationHelper with {(i + 1, array, permutations)}")
            permutationHelper(i + 1, array, permutations)
            swap(array, i , j)
            # print(f"Array after swapping2 : {array}")

        

def swap(array, i , j):
    array[i], array[j] = array[j], array[i]



## perumation without swapping
def permutaiton2(array):
    allPermutations = []
    permutation2Helper(array, [], allPermutations)
    return allPermutations

def permutation2Helper(array, perm, permutations):
    if len(array) == 0 and len(perm):
        permutations.append(perm)

    else:

        for i in range(len(array)):
            newArray = array[:i] + array[i+1: ]
            newPerm = perm + [array[i]]
            permutation2Helper(newArray, newPerm, permutations)



if __name__ == '__main__':
    n = [1,2,3]
    print(f"Printing all permutations of list {n} : {permutaiton(n)}")
    # s = "abc"
    # perm_s = [''.join(i) for i in permutaiton(list(s))]
    # print(f"Printing all {len(perm_s)} permutations of string {s} : {perm_s}")


    print(f"Printing all permutations of list {n} : {permutaiton2(n)}")

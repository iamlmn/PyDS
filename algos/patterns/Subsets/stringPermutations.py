# Given a string, find all of its permutations preserving the character sequence but changing case.

# Example 1:

# Input: "ad52"
# Output: "ad52", "Ad52", "aD52", "AD52" 
# Example 2:

# Input: "ab7c"
# Output: "ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"

#iterative_approach
from collections import deque
def getStringPermutations(input_string):
    result = []
    result.append(input_string)

    for i in range(len(input_string)):
        if input_string[i].isalpha():
            # print(input_string[i])
            for j in range(len(result)):
                t = list(result[j])
                t[i] = t[i].swapcase()
                result.append(''.join(t))

    return result

if __name__ == '__main__':
    str1 = "ad52"
    str2 = "ab7c"
    r1 = getStringPermutations(str1)
    r2 = getStringPermutations(str2)
    print(r1)
    print(r2)
    assert r1 == ["ad52", "Ad52", "aD52", "AD52"]
    assert r2 == ["ab7c", "Ab7c", "aB7c", "AB7c", "ab7C", "Ab7C", "aB7C", "AB7C"]
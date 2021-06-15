# Every non-negative integer N has a binary representation, for example, 8 can be represented as “1000” in binary and 7 as “0111” in binary.

# The complement of a binary representation is the number in binary that we get when we change every 1 to a 0 and every 0 to a 1. For example, the binary complement of “1010” is “0101”.

# For a given positive number N in base-10, return the complement of its binary representation as a base-10 integer.

# Example 1:

# Input: 8
# Output: 7
# Explanation: 8 is 1000 in binary, its complement is 0111 in binary, which is 7 in base-10.
# Example 2:

# Input: 10
# Output: 5
# Explanation: 10 is 1010 in binary, its complement is 0101 in binary, which is 5 in base-10.


def getComplement(num):
    '''
    Time: O(b) where b is the number of bits used to represent a number.
    Space: O(1)
    '''

    # first we need to  get the all_set bits
    bit_count = 0
    d = num
    while d > 0:
        bit_count += 1
        d = d >> 1
    all_set_bits = pow(2, bit_count) - 1


    return all_set_bits ^ num

if __name__ == '__main__':

    num1 = 8 
    num2 = 10

    r1 = getComplement(num1)
    r2 = getComplement(num2)

    print(r1, r2)
    assert r1 == 7
    assert r2 == 5


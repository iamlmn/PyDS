# Given two strings containing backspaces (identified by the character ‘#’), check if the two strings are equal.

# Example 1:

# Input: str1="xy#z", str2="xzz#"
# Output: true
# Explanation: After applying backspaces the strings become "xz" and "xz" respectively.
# Example 2:

# Input: str1="xy#z", str2="xyz#"
# Output: false
# Explanation: After applying backspaces the strings become "xz" and "xy" respectively.
# Example 3:

# Input: str1="xp#", str2="xyz##"
# Output: true
# Explanation: After applying backspaces the strings become "x" and "x" respectively.
# In "xyz##", the first '#' removes the character 'z' and the second '#' removes the character 'y'.
# Example 4:

# Input: str1="xywrrmp", str2="xywrrmu#p"
# Output: true
# Explanation: After applying backspaces the strings become "xywrrmp" and "xywrrmp" respectively.


def compareString(stringInput1, stringInput2):
    index1 = len(stringInput1) - 1
    index2 = len(stringInput2) - 1

    while index1 >=0 or index2 >= 0:
        i1 = getNextValidCharacter(stringInput1, index1)
        i2 = getNextValidCharacter(stringInput2, index2)

        if i1<0 and i2 <0:
            return True

        if i1 < 0 or i2 < 0:
            return False

        if stringInput1[i1] != stringInput2[i2]:
            return False

        index1 = i1 -1
        index2 = i2 - 1

    return True




def getNextValidCharacter(string1, index):
    backSpaceCount = 0
    while index >= 0:
        if string1[index] == '#':
            backSpaceCount += 1
        elif backSpaceCount > 0:
            backSpaceCount -= 1
        else:
            break
        index -= 1
    return index


if __name__ == '__main__':
    str1="xy#z"
    str2="xzz#"
    print(f"{str1} == {str2} ? : {compareString(str1 , str2)}")


    str11="xy#z"
    str21="xyz#"
    print(f"{str11} == {str21} ? : {compareString(str11 , str21)}")

    str21="xp#"
    str22="xyz##"
    print(f"{str21} == {str22} ? : {compareString(str21 , str22)}")


    str31="xywrrmp"
    str32="xywrrmu#p"
    print(f"{str31} == {str32} ? : {compareString(str31 , str32)}")
            


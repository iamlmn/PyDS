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



def applyBackspace(stringInput):
    # prev = 0
    i = 0
    high = len(stringInput) - 1
    while i <= high:
        # prev = i - 1
        if stringInput[i] == '#':
            stringInput = stringInput[:i - 1] + stringInput[i + 1:]
            high -= 2
            i -= 1
        else:
            i += 1
    return stringInput[:high + 1]


def checkString(string1, string2):
    return applyBackspace(string1) == applyBackspace(string2)


if __name__ == '__main__':
    str1="xy#z"
    str2="xzz#"
    print(f"{str1} == {str2} ? : {checkString(str1 , str2)}")


    str11="xy#z"
    str21="xyz#"
    print(f"{str11} == {str21} ? : {checkString(str11 , str21)}")

    str21="xp#"
    str22="xyz##"
    print(f"{str21} == {str22} ? : {checkString(str21 , str22)}")


    str31="xywrrmp"
    str32="xywrrmu#p"
    print(f"{str31} == {str32} ? : {checkString(str31 , str32)}")
            


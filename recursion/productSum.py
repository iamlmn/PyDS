
def productSum(array, multiplier=1):
    s = 0
    p =1

    for i in array:
        if type(i) is not list:
            s += i
        else: 
            s += productSum(i, multiplier + 1)

    return s*multiplier



if __name__ == '__main__':
    array = [5, 2, [7, -1 ], 3, [6, [-13, 8], 4]]
    x1 = productSum(array)
    print(f"prodcutSum of {array} is {x1}")
    assert x1 == 12
# Any number will be called a happy number if, after repeatedly replacing it with 
# a number equal to the sum of the square of all of its digits, leads us to number ‘1’.
#  All other (not-happy) numbers will never reach ‘1’. Instead, they will be stuck in a 
#  cycle of numbers which does not include ‘1’.
global z
z = [ ]
def find_happyNumber(num):
    slow, fast = num, num 
    while True:
        slow = find_sum(slow)
        fast = find_sum(find_sum(fast))
        if slow == fast:
            break
    return slow == 1

def find_sum(num):
    _sum = 0

    while num > 0:
        digit = num % 10
        _sum += digit * digit 
        num //= 10

    return _sum



if __name__ == '__main__':
    #Sup

    print(f"{find_happyNumber(23)}")
    print(f"{find_happyNumber(12)}")
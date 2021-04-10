# LIFO Stack DS using Python Lists (Arrays)
class StacksArray:

    def __init__(self):
        self.stackArray = []

    def __len__(self):
        return len(self.stackArray)
    
    def isempty(self):
        return len(self.stackArray) == 0

    def display(self):
        print(self.stackArray)

    def top(self):
        return self.stackArray[-1]

    def pop(self):
        if self.isempty():
            print("Stack is empty")
            return None
        return self.stackArray.pop()

    def push(self, element):
        self.stackArray.append(element)
        

if __name__ =='__main__':
    
    S = StacksArray()
    S.push(5)
    S.push(3)
    S.display()
    print(len(S))
    print(S.pop())
    print(S.isempty())
    print(S.pop())
    print(S.isempty())
    S.push(7)
    S.push(9)
    print(S.top())
    S.push(4)
    print(len(S))
    print(S.pop())
    S.push(6)
    S.push(8)
    print(S.pop())


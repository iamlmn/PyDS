# Recursion

Complexity can solved using Recurrence relation , ->  Subsitituion or 
Types of recursion 

1. Tail & head.
    - If all the things need to be executed are above recursive call - Tail recursion
    - If the recursion call is on the head of the fm -> Head recursion. 

    In a recursive logic to print square numbers,

    Tail recursion output : 1, 4, 9, 16
    Head recursion output : 16, 9, 4, 1
2. Tree Recursion.
 - When a function calls itself more than once

 ```python
    def calculate( n):
        if n> 0:
            calculate(n-1)
            k =  n** 2
            print(k)
            calculate(n - 1)
 ``` 

  The above method for n = 3 calls the fn 15times.
  Generally Time complexity = O(2^n), (2^0 + 2^1 + 2^2 ... 2^n)
3. Indirect recursion
 - A function which may call other function recursivly:
 Example : 
    
    ```python
    def calA(n):
        if n > 0:
            calB(n-1)

    def calB(n):
    if n == 0:
        return 2
    else:
        return calA(n - 1)
    ```



## Sum of n numbers
##### Time complexity : O(n))
```python
def sumrec(n):
    if n == 0:
        return 0
    return sumrec(n-1) + n

```


## Factorial of n numbers
##### Time complexity : O(n))
```python
def fact(n):
    if n == 1:
        return 1
    return fact(n - 1) * n

```


## Fibonnaci of n
a = 0, b = 1
```python
def fibFun(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibFun(n - 1) + fibFun(n-2) 
```
#Sum of n natural numbers
#Traditional Approach
def Natural_Sum(n):
    s = 0
    for i in range(n,0,-1):
        s += i
    return s

print(Natural_Sum(5))
print(Natural_Sum(10))

# Recursive Approach
def Natural_Sum1(n):
    if n == 1:
        return 1
    else:
        return n + Natural_Sum1(n-1)
    
print(Natural_Sum1(5))
print(Natural_Sum1(10))    

#Find factorial of a number
#Traditional Approach
def Factorial(n):
    f = 1
    for  i in range(n,0,-1):
        f *= i
    return f

print(Factorial(5))#120
print(Factorial(3))#6

def Factorial1(n):
    if n < 0:
        return "No factorial -ve numbers"
    elif n==0 or n == 1:
        return 1
    else:
        return n * Factorial1(n-1)

print(Factorial1(5))#120
print(Factorial1(3))#6

#Fibonacci series
def Fibonacci(n):
    if n <= 0:
        return "Provide a +ve number"
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return Fibonacci(n-2) + Fibonacci(n-1)

print(Fibonacci(5))#3

#GCD of two numbers
#Traditional Approach
def GCD(a,b):
    while b != 0:
        a,b = b,a%b
    return a 

print(GCD(4,10))
# Recursive Approach
def GCD1(a,b):
    if b == 0:
        return a
    return GCD1(b,a%b)

print(GCD1(4,10))
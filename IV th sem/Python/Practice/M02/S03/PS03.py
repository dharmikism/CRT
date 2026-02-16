'''
# Problem 1: Arithmetic Progression
# Problem Statement: Generate first 10 terms of an AP given first term 'a' and common difference 'd'
# Input: Two integers a (first term) and d (common difference), separated by space
# Output: First 10 terms of the AP separated by space
a,d=map(int,input().split())
for i in range(1,11):
    print(a+(i-1)*d,end=" ")
print()

# Problem 2: Geometric Progression
# Problem Statement: Generate first 10 terms of a GP given first term 'a' and common ratio 'r'
# Input: Two integers a (first term) and r (common ratio), separated by space
# Output: First 10 terms of the GP separated by space
a,r=map(int,input().split())
for i in range(1,11):
    print(a*(r**(i-1)),end=" ")
print()

# Problem 3: Fibonacci Sequence
# Problem Statement: Generate first n terms of the Fibonacci sequence where each term is sum of previous two terms
# Input: Integer n (number of terms required)
# Output: First n terms of Fibonacci sequence separated by space
a=0
b=1
n=int(input())
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b 
    b=c 
print()

# Problem 4: Sequence Type Checker
# Problem Statement: Identify if three given numbers form an AP, GP, Fibonacci sequence, or Pythagorean triplet
# Input: Three integers a, b, c separated by space
# Output: Type of sequence/triplet (AP, GP, FIB, or Pythagorean Triplet)
a,b,c=map(int,input().split())
if b-a==c-b:
    print("AP")
elif b/a==c/b:
    print("GP")
elif a+b==c:
    print("FIB")
elif a**2+b**2==c**2:
    print("Pythagorean Triplet")
print()

# Problem 5: Fibonacci Sequence (Using List)
# Problem Statement: Generate first n terms of the Fibonacci sequence using a list and store all terms
# Input: Integer n (number of terms required)
# Output: All n Fibonacci terms separated by space
l=[0,1]
n=int(input())
for i in range(2,n):
    c=l[i-2]+l[i-1]
    l.append(c)
print(*l)
'''

# Problem 6: Factorial Calculation
# Problem Statement: Calculate the factorial of a given number n using recursion
# Input: Integer n (number to calculate factorial for)
# Output: Factorial of n

def fact(n):
    if n<0:
        return "Factorial not defined for negative numbers"
    elif n==0 or n==1:
        return 1
    else:
        return n*fact(n-1)

n=int(input())
print(fact(n))
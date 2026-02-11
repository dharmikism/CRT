'''
Write a Python program to count the number of digits in a given number using both manual iterative method and built-in len() method.

n=int(input("Enter a number: "))
c=0
d=str(n)
while n>0:
    n=n//10
    c+=1
print("Number of digits(Manual Iterative Method): ",c)
print("Number of digits(Len Method): ",len(d))

Write a Python program to calculate the sum of digits in a given number:

n=int(input("Enter a number: "))
s=0
while n>0:
    s+=n%10
    n=n//10
print("Sum of digits: ",s)

Write a Python program to extract and display the even digits from a given number:

n=int(input("Enter a number: "))
l=""
while n>0:
    if n%10%2==0:
        l+=str(n%10)+" "
    n=n//10
print(l[len(l)-1::-1])

Write a Python program to reverse the digits of a given number:

n=int(input("Enter a number: "))
r=0
while n>0:
    r=r*10+n%10
    n=n//10
print("Reversed number: ",r)

Write a Python program to check if a given number is a palindrome:
n=int(input("Enter a number: "))
temp=n
r=0
while n>0:
    r=r*10+n%10
    n=n//10
if temp==r:
    print("The number is a palindrome.")

Write a Python program to determine if its Armstrong number or not:
n=int(input("Enter a number: "))
s=0
temp=n
while temp>0:
    s+=pow(temp%10,3)
    temp=temp//10
if s==n:
    print("The number is an Armstrong number.")
else:
    print("The number is not an Armstrong number.")
'''
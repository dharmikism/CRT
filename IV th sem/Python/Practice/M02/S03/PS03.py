'''
a,d=map(int,input().split())
for i in range(1,11):
    print(a+(i-1)*d,end=" ")

a,r=map(int,input().split())
for i in range(1,11):
    print(a*(r**(i-1)),end=" ")

a=0
b=1
n=int(input())
print(a,b,end=" ")
for i in range(2,n):
    c=a+b
    print(c,end=" ")
    a=b 
    b=c 

a,b,c=map(int,input().split())
if b-a==c-b:
    print("AP")
elif b/a==c/b:
    print("GP")
elif a+b==c:
    print("FIB")
elif a**2+b**2==c**2:
    print("Pythagorean Triplet")
'''
l=[0,1]
n=int(input())
for i in range(2,n):
    c=l[i-2]+l[i-1]
    l.append(c)
print(*l) 
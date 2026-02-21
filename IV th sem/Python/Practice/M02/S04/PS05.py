'''
n=int(input())
for i in range(n):
    for j in range(n):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()


n=int(input())
for i in range(n):
    if i==0 or i==n-1:
        print("* "*n)
    else:
        print("*"+" "*(n-1)+"*")  

Probelm : Inverted Right-Angled Triangle
n=int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end=" ")
    print()




Problem : hollow circle
'''
n=int(input())
for i in range(n):
    for j in range(n):
        if (i==0 or i==n-1) and (j>0 and j<n-1):
            print("*",end=" ")
        elif (j==0 or j==n-1) and (i>0 and i<n-1):
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()


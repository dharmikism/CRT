'''

Write a function that generates the first n rows of Pascal's triangle.

1
1 1
1 2 1
1 3 3 1
1 4 6 4 1


n=int(input())
li=[[1]*n for i in range(n)]
print(li[0][0])
for i in range(1,n):
    for j in range(i+1):
        if j==0 or j==i:
            li[i][j]=1
        else:
            li[i][j]=li[i-1][j-1]+li[i-1][j]
        print(li[i][j],end=" ")
    print()



n=int(input())
if n%2==0:
    isEven=True
for i in range(1,n+1):
    if i<=n//2:
        print("*"*(i)+" "*(n-2*(i))+"*"*(i))
    else:
        print("*"*(n-i)+" "*(2*(i)-n)+"*"*(n-i))

'''
x=[1,2]
y=x
x.append(3)
print(x)
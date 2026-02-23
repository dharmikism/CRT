'''
li=[1,2,3,4,5]
output=[1,4,9,16,25]

li=list(map(int,input().split()))
print(*list(map(lambda x:x**2,li)))

input = [1,2,3,4,5]
output-[2,4]

li=list(map(int,input().split()))
print(*list(filter(lambda x:x%2==0,li)))

input=['d','h','a','r','m','i','k']
output= dharmik

li=list(input().split())
print("".join(li))

n=int(input())
for i in range(n):
    print(" "*(n-i-1)+"* "*(i+1))


n=int(input())
for i in range(n):
    print(" "*(i)+"* "*(n-i))

n=int(input())
li=[i for i in range(1,n+1)]
for i in range(n):
    print(" "*(n-i-1)+" ".join(map(str,li[:i+1])))
'''

n=int(input())
for i in range(n):
    if i!=(n-1):
        print(" "*(n-i-1)+"* "+" "*(i*2-2)+"* "*(i>0))
    else:
        print("*"*(n*2-1))
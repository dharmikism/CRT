'''
Print all the factors 

n=int(input())
s=""
for i in range(1,n//2+1):
    if n%i==0:
        s+=str(i)+" "
s+=str(n)
print(s)


n=int(input())
cond=True
for i in range(2,n//2+1):
    if n%i==0:
        cond=False
print("Prime" if cond else "Not Prime")

a, b = map(int, input().split())

for i in range(a, b + 1):
    if i < 2:
        continue
    cond = True
    for j in range(2, int(i ** 0.5) + 1):
        if i % j == 0:
            cond = False
            break
    if cond:
        print(i, end=" ")

def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)
    
print(fact(int(input())))
'''
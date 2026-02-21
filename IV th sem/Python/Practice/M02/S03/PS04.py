def strong(n):
    s=0
    temp=n
    while temp>0:
        f=1
        for i in range(1,temp%10+1):
            f*=i
        s+=f
        temp=temp//10
    if s==n:
        return "The number is a Strong number."
    else:
        return "The number is not a Strong number."
n=int(input())
print(strong(n))

def perfect(n):
    s=0
    for i in range(1,n):
        if n%i==0:
            s+=i
    if s==n:
        return "The number is a Perfect number."
    else:
        return "The number is not a Perfect number."
n=int(input())
print(perfect(n))
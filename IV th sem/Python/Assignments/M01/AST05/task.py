from typing import List


def Collatz_Sequence(n: int)-> List:
   l=[]
   while n!=1:
       l.append(n)
       if n%2==0:
           n=n//2
       else:
           n=3*n+1
   l.append(1)
   return l
if __name__ == '__main__':
    n = int(input())
    print(Collatz_Sequence(n))
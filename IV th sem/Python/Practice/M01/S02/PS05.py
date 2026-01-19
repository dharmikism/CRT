counter=0
while counter<5:
    print("Counter value:",counter)
    counter+=1

x,y=map(int,input("Enter two numbers: ").split())
for i in range(x,y+1):
    if i%2==0:
        print(i,end=" ")

while x<y:
    if x%2!=0:
        print(x,end=" ")
    x+=1

dhar=int(input())
if dhar%3==0:
    print("fizz")
elif dhar%5==0:
    print("buzz")
elif dhar%3==0 and dhar%5==0:
    print("fizzbuzz")
#Digital root sum
#386 ==> 17 ==> 8
def Digital_Sum(n):
    if n <= 9:
        return n
    s = sum([int(ch) for ch in str(n)])
    return Digital_Sum(s)

print(Digital_Sum(386))#8

#Sorted check
def Sorted_Array(nums):
    pass

print(Sorted_Array([10,20,30,40,50]))#True
print(Sorted_Array([10,4,30,25,50]))#False

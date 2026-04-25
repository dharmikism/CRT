from collections import Counter
def freq(nums):
    d = {}
    for i in nums:
        if i in d:
            d[i] += 1
        else:
            d[i] = 1
    return d

def uniq(nums):
    l=[]
    for i in nums:
        if i in l:
            continue
        l.append(i)
    return l

def max_freq(nums):
    print(Counter(nums).most_common(1))

print(max_freq([1,4,2,1,3,5,2]))
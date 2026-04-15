#Dictionary
'''
1. keys should be immutable ==> Numeric DT,Bool,Str,Tuple
2. keys should be unique

d = {1:'a',2:'b',3:'c',1:'z'}
print(d)
'''
#217. Contains Duplicate
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))

#349. Intersection of Two Arrays
def intersection1(nums1,nums2):
    s1 = set(nums1)
    s2 = set(nums2)
    print(list(s1.intersection(s2)))

intersection1([1,2,2,1],[2,2])

#Leetcode-387 ==> First Unique Character in a String
from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        freq = dict(Counter(s))
        for i,ch in enumerate(s):
            if freq[ch] == 1:
                return i
        return -1
    
# Leetcode - 1 ==> Two Sum
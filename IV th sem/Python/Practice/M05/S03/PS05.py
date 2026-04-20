from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        def backtrack(index, curr):
            if index == len(nums):
                res.append(curr[:])
                return

            curr.append(nums[index])
            backtrack(index + 1, curr)

            curr.pop()
            backtrack(index + 1, curr)

        backtrack(0, [])
        return res
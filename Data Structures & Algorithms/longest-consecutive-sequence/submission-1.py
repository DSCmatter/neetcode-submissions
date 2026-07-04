class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        res = 0

        for num in nums:
            count = 0 
            curr = num 
            while curr in hashset:
                count += 1 
                curr += 1 
            res = max(res, count)
        return res
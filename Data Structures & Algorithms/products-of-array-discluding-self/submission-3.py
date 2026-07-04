class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        n = len(nums)
        for i in range(n):
            prod = 1
            for j in range(n):
                if j != i:
                    prod = prod * nums[j]
            res.append(prod)
        return res
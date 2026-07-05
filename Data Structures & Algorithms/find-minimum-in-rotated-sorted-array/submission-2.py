class Solution:
    def findMin(self, nums: List[int]) -> int:
        res = nums.sort()
        return nums[0]
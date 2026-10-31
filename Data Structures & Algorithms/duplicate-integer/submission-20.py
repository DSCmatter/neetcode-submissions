class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Myset = set()

        for num in nums:
            if num in Myset:
                return True 

            Myset.add(num)

        return False
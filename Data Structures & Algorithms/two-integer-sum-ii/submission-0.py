class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers) - 1 

        while l < r:
            curSum = numbers[l] + numbers[r] 

            if curSum > target:
                r -= 1 
            elif curSum < target:
                l += 1 
            else: # curSum is qual to target, return the indices left and right but they're based on 1, so we add 1 
                return [l + 1, r + 1]
        return []
            
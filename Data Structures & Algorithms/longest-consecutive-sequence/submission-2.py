class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hashset = set(nums)
        longest = 0 

        for num in hashset:
            if num - 1 not in hashset: 
                # Only start counting if this is the beginning of a sequence
                current = num
                length = 1 
                
                # keep extending the sequence 
                while current + 1 in hashset:
                    current += 1 
                    length += 1 

                longest = max(longest, length)

        return longest 

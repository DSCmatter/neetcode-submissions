class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        seen = {}
        max_len = -1 

        for i, char in enumerate(s): 
            if char in seen: 
                cur_len = i - seen[char] - 1 
                max_len = max(max_len, cur_len)
            else: 
                seen[char] = i
        return max_len
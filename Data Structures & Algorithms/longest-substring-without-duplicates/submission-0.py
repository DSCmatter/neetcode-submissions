class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res = 0 
        for i in range(len(s)):
            hashset = set()
            for j in range(i, len(s)):
                if s[j] in hashset:
                    break 
                hashset.add(s[j])
            res = max(res, len(hashset))
        return res
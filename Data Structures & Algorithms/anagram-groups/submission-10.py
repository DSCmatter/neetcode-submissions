class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            # Sort the characters of the string to form a key.
            sortedS = ''.join(sorted(s))
            # Append the original string to the list corresponding to this key.
            res[sortedS].append(s)
        return list(res.values())
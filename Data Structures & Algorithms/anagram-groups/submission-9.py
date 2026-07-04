class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        for s in strs:
            newStr = ''.join(sorted(s))
            res[newStr].append(s)
        return list(res.values())
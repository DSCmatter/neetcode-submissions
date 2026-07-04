class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = []

        for word in strs:
            found = False 
            for group in res:
                if sorted(group[0]) == sorted(word):
                    group.append(word)
                    found = True 
                    break
            if not found:
                res.append([word])
        return res 
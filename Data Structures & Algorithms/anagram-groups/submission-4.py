class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {} # mapping the charCount to list of Anagrams 

        for s in strs: 
            sortedStr = ''.join(sorted(s))

            if sortedStr not in res:
                res[sortedStr] = []
            res[sortedStr].append(s)

        return res.values()

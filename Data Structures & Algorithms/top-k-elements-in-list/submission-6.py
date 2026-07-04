class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for num in nums:
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 
        
        def getFreq(item):
            return item[1]
        
        sortedElements = sorted(freq.items(), key=getFreq, reverse=True)

        return [item[0] for item in sortedElements[:k]]
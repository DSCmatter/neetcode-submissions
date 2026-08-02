class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        # O(n) 
        # instead of counting each num by scanning we update count as we iterate 
        for num in nums:    
            if num in freq:
                freq[num] += 1 
            else:
                freq[num] = 1 
            
        return sorted(freq, key=freq.get, reverse=True)[:k]


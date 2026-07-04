from collections import Counter 

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)

        def getFreq(item):
            return item[1]

        sortedElements = sorted(count.items(), key=getFreq, reverse=True)

        return [item[0] for item in sortedElements[:k]]
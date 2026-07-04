from collections import Counter
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        
        # Correcting the method name to most_common
        most_common = count.most_common(k)
        
        # Returning only the elements of the most common items
        return [element for element, frequency in most_common]

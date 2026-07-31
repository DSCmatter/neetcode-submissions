class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hashset = set()
        freq = {}

        for num in nums:
            if num not in hashset:
                hashset.add(num)
                count = 0 
                for i in nums:
                    if i == num:
                        count += 1 
                freq[num] = count

        return sorted(freq, key=freq.get, reverse=True)[:k]
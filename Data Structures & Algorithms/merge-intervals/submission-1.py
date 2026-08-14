class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n)
        intervals.sort(key= lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1] # get the most recently added value and the end value of it bc we need it to know if it overlaps.

            if start <= lastEnd: # if overlap 
                output[-1][1] = max(lastEnd, end)
            # [1, 5], [2, 4] = [1, 5] reason why we take max
            else: # if non overlap 
                output.append([start, end])

        return output 
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # O(n log n)
        intervals.sort(key= lambda i: i[0])
        output = [intervals[0]]

        for start, end in intervals[1:]:
            lastEnd = output[-1][1]

            if start <= lastEnd: # if overlap 
                output[-1][1] = max(lastEnd, end)
            else: # if non overlap 
                output.append([start, end])

        return output 
            # [1, 5], [2, 4] = [1, 5]
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort()

        res = 0 # count of remoiving intervals 
        prevEnd = intervals[0][1] # end value of first interval  
        for i in range(1, len(intervals)): # Iterate through the intervals starting from the second one
            if prevEnd > intervals[i][0]:
                res += 1 
                # Keep the interval that ends earlier
                # This leaves more room for future intervals
                prevEnd = min(prevEnd, intervals[i][1])
                
            else:
                prevEnd = intervals[i][1]
        return res
"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        # use two ptrs
        start = sorted([i.start for i in intervals])
        end = sorted([i.end for i in intervals])

        res, count = 0, 0 
        s, e = 0, 0 # start, end

        while s < len(intervals): # while s has not reached end of intervals
            if start[s] < end[e]: # start pos in array is less than pos at end
                # we need another room
                s += 1 
                count += 1 
            else:
                # meeting has ended so we have free room 
                e += 1 
                count -= 1  
            res = max(res, count) # maximum meeting rooms 
        return res

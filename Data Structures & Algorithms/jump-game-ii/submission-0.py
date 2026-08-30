class Solution:
    def jump(self, nums: List[int]) -> int:
        res = 0
        l, r = 0, 0 # to determine what lvl of bfs we at 

        # 1D array, simplified bfs 
        while r < len(nums) - 1:
            farthest = 0 
            for i in range(l, r + 1):
                farthest = max(farthest, i + nums[i]) # whats the farthest location we can jump to 
            # update our window 
            l = r + 1 
            r = farthest 
            res += 1 
        return res

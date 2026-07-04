class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:

        #Let res store the number of days until a warmer temperature.
        # For each index i:
            # Start checking from the next day j = i + 1 and count how many steps it takes to find a warmer day.
            # If a warmer day is found, store the count.
            # Otherwise, store 0.
        # Return the result array. 
        res = []
        n = len(temperatures)

        for i in range(n):
            count = 1 
            j = i + 1 
            while j < n:
                if temperatures[j] > temperatures[i]:
                    break
                j += 1 
                count += 1 
            count = 0 if j == n else count 
            res.append(count)
        return res

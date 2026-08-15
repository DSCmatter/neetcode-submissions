class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # staircase search 
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            # Start from top-right corner
            if matrix[top][right] > target:
                right -= 1 # If the value is greater than the target, move left (right -= 1).
            elif matrix[top][right] < target:
                top += 1 # If the value is smaller, move down (top += 1).
            else:
                return True

        return False
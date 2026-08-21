class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking 
        ROWS, COLS = len(board), len(board[0])
        path = set()

        def dfs(r, c, i):
            if i == len(word): #  all characters matched → return true.
                return True 

            # if out of bounds
            if (min(r, c) < 0 or
                r >= ROWS or c >= COLS or
                word[i] != board[r][c] or
                (r, c) in path):
                return False # mismatch or already visited → return false.
            
            path.add((r, c)) # Mark (row, col) as visited.
            res = (dfs(r + 1, c, i + 1) or # Recurse to 4 neighbors with i + 1.
                   dfs(r - 1, c, i + 1) or
                   dfs(r, c + 1, i + 1) or
                   dfs(r, c - 1, i + 1))
            path.remove((r, c)) # Unmark (row, col) (backtrack).
            return res
            
        # If any start cell returns true, answer is true; otherwise false.
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True 
        return False 
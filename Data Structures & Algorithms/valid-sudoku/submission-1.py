class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        # Check rows
        for r in range(9):
            seen = set()
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Check columns
        for c in range(9):
            seen = set()
            for r in range(9):
                if board[r][c] == ".":
                    continue
                if board[r][c] in seen:
                    return False
                seen.add(board[r][c])

        # Check 3×3 sub-boxes
        for box in range(9):
            seen = set()
            for i in range(3):
                for j in range(3):
                    r = (box // 3) * 3 + i
                    c = (box % 3) * 3 + j
                    if board[r][c] == ".":
                        continue
                    if board[r][c] in seen:
                        return False
                    seen.add(board[r][c])

        return True

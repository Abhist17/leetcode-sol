from typing import List

class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        m, n = len(grid), len(grid[0])

        total = sum(sum(row) for row in grid)

        # -------- Horizontal --------
        bottom_set = set()
        for row in grid:
            for x in row:
                bottom_set.add(x)

        top_set = set()
        curr = 0

        for i in range(m - 1):
            row = grid[i]

            for x in row:
                top_set.add(x)

            curr += sum(row)
            other = total - curr

            if curr == other:
                return True

            diff = abs(curr - other)

            if curr > other:
                if diff in top_set:
                    if self.valid_row(grid, 0, i, diff):
                        return True
            else:
                if diff in bottom_set:
                    if self.valid_row(grid, i+1, m-1, diff):
                        return True

        # -------- Vertical --------
        right_set = set()
        for j in range(n):
            for i in range(m):
                right_set.add(grid[i][j])

        left_set = set()
        col_sum = [sum(grid[i][j] for i in range(m)) for j in range(n)]

        curr = 0

        for j in range(n - 1):
            for i in range(m):
                left_set.add(grid[i][j])

            curr += col_sum[j]
            other = total - curr

            if curr == other:
                return True

            diff = abs(curr - other)

            if curr > other:
                if diff in left_set:
                    if self.valid_col(grid, 0, j, diff):
                        return True
            else:
                if diff in right_set:
                    if self.valid_col(grid, j+1, n-1, diff):
                        return True

        return False

    def valid_row(self, grid, r1, r2, diff):
        rows = r2 - r1 + 1
        cols = len(grid[0])

        if rows > 1 and cols > 1:
            return True

        if rows == 1:
            row = grid[r1]
            return row[0] == diff or row[-1] == diff

        if cols == 1:
            return grid[r1][0] == diff or grid[r2][0] == diff

        return False

    def valid_col(self, grid, c1, c2, diff):
        rows = len(grid)
        cols = c2 - c1 + 1

        if rows > 1 and cols > 1:
            return True

        if cols == 1:
            return grid[0][c1] == diff or grid[-1][c1] == diff

        if rows == 1:
            row = grid[0]
            return row[c1] == diff or row[c2] == diff

        return False
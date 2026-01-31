# Last updated: 1/31/2026, 2:18:41 PM
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        row_hashmap = {}
        result = 0

        # Traverse through the rows and update the row hashmap
        for i, row in enumerate(grid):
            row_key = tuple(row)
            if row_key in row_hashmap:
                row_hashmap[row_key] += 1
            else:
                row_hashmap[row_key] = 1

        # Traverse through the columns and compare with row hashmap
        for j in range(len(grid[0])):
            col_key = tuple(grid[i][j] for i in range(len(grid)))
            if col_key in row_hashmap:
               result += row_hashmap[col_key]

        return result
           
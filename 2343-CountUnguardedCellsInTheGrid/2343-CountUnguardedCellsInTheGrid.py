# Last updated: 1/31/2026, 2:18:42 PM
from typing import List

class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:

        # This makes the code self-documenting.
        EMPTY = 0
        GUARD = 1
        WALL = 2
        GUARDED = 3 
        
        grid = [[EMPTY] * n for _ in range(m)]
        
        # --- 2. Place guards and walls on the grid ---
        for r, c in guards:
            grid[r][c] = GUARD
        for r, c in walls:
            grid[r][c] = WALL
        
        # --- 3. Define the function to "shine light" from a guard ---
        def mark_cells_as_guarded(r_guard, c_guard):
            
            # Helper to check if light is blocked by a wall or another guard
            def is_blocker(row, col):
                return grid[row][col] == WALL or grid[row][col] == GUARD

            # Look DOWN (increasing row)
            for r in range(r_guard + 1, m):
                if is_blocker(r, c_guard):
                    break
                grid[r][c_guard] = GUARDED
            
            # Look UP (decreasing row)
            for r in reversed(range(0, r_guard)):
                if is_blocker(r, c_guard):
                    break
                grid[r][c_guard] = GUARDED

            # Look RIGHT (increasing col)
            for c in range(c_guard + 1, n):
                if is_blocker(r_guard, c):
                    break
                grid[r_guard][c] = GUARDED

            # Look LEFT (decreasing col)
            for c in reversed(range(0, c_guard)):
                if is_blocker(r_guard, c):
                    break
                grid[r_guard][c] = GUARDED

        # --- 4. Run the "mark as guarded" process for every guard ---
        for r, c in guards:
            mark_cells_as_guarded(r, c)
        
        # --- 5. Count the remaining empty (unguarded) cells ---
        unguarded_count = 0
        
        # (Using 'row' and 'cell_state' is clearer than 'r' and 'n')
        for row in grid:
            for cell_state in row:
                if cell_state == EMPTY:
                    unguarded_count += 1
        
        return unguarded_count
# Last updated: 1/31/2026, 2:18:24 PM
from typing import List

class Solution:
    def separateSquares(self, squares: List[List[int]]) -> float:
        # 1. Pre-calculation: Calculate total area and the vertical bounds of the search
        total_area = 0.0
        min_y = float('inf')
        max_y = float('-inf')
        
        for x, y, l in squares:
            total_area += l * l
            min_y = min(min_y, y)
            max_y = max(max_y, y + l)
            
        # The line must be between the lowest y and the highest y+l
        lo, hi = min_y, max_y
        
        def get_area_below(limit_y: float) -> float:
            """
            Calculates the total area of all squares lying below the horizontal line y = limit_y.
            """
            area = 0.0
            for x, y, l in squares:
                # If the square is entirely above the line, it contributes 0
                if y >= limit_y:
                    continue
                # If the square is entirely below the line, it contributes its full area (l*l)
                # If it is partially below, the height below the line is (limit_y - y)
                # We use min(limit_y - y, l) to handle both partial and full coverage
                height_below = min(limit_y - y, float(l))
                area += l * height_below
            return area

        # 2. Binary Search
        # Using an epsilon (eps) threshold to determine when the range has 
        # narrowed sufficiently to meet the precision requirements.
        eps = 1e-5
        while hi - lo > eps:
            mid = (lo + hi) / 2
            
            # If the area below 'mid' is at least half of the total area,
            # then the line we need is either at 'mid' or below it.
            if get_area_below(mid) >= total_area / 2.0:
                hi = mid
            else:
                lo = mid
                
        # Returning 'hi' as the converged value.
        return hi
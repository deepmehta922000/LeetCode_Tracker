# Last updated: 1/31/2026, 2:18:31 PM
class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        maxDiag = -1
        maxArea = -1

        for a, b in dimensions:
            diag = a*a + b*b     
            area = a*b
            if diag > maxDiag or (diag == maxDiag and area > maxArea):
                maxDiag = diag
                maxArea = area

        return maxArea

# Last updated: 1/31/2026, 2:18:47 PM
class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0 

        for o in operations:
            if o[1] == "+":
                s += 1
            else:
                s -= 1
        
        return s
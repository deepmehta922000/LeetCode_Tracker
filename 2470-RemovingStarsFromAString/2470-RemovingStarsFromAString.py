# Last updated: 1/31/2026, 2:18:40 PM
# class Solution:
#     def removeStars(self, s: str) -> str:
        
#         while "*" in s:
#             index = s.index("*")
#             s = s[:index-1] + s[index+1:]
#             self.removeStars(s)
        
#         return s

class Solution:
    def removeStars(self, s: str) -> str:
        output=[]
        for c in s:
            if c is not "*":
                output.append(c)
            else:
                output.pop()
        
        return "".join(output)
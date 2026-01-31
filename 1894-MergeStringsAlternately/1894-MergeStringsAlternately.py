# Last updated: 1/31/2026, 2:18:59 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        length1 = len(word1)
        length2 = len(word2)
        i = 0
        j = 0
        output = ""
        while length1 > i or length2 > j:
            if i < length1:
                output = output + word1[i]
                i += 1
            if j < length2:
                output = output + word2[j]
                j += 1
        
        return output
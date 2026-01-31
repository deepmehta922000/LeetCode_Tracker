# Last updated: 1/31/2026, 2:19:01 PM
class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        currAltitude = 0
        maxAltitude = 0
        for i in gain:
            currAltitude += i
            maxAltitude = max(currAltitude,maxAltitude)
        return maxAltitude
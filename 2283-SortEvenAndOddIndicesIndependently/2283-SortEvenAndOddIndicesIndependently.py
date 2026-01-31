# Last updated: 1/31/2026, 2:18:43 PM
class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        odds = []
        evens = []

        for i, num in enumerate(nums):
            if i % 2 == 0:
                evens.append(num)
            else:
                odds.append(num)

        odds.sort(reverse=True)
        evens.sort()

        oddIndex, evenIndex = 0, 0
        for i in range(len(nums)):
            if i % 2 == 0:
                nums[i] = evens[evenIndex]
                evenIndex += 1
            else:
                nums[i] = odds[oddIndex]
                oddIndex += 1

        return nums
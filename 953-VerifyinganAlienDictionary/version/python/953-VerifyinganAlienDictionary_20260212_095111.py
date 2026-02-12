# Last updated: 2/12/2026, 9:51:11 AM
1class Solution:
2    def isAlienSorted(self, words: List[str], order: str) -> bool:
3        order_index = { c : i for i, c in enumerate(order)}
4
5        for i in range(len(words) - 1):
6            w1, w2 = words[i], words[i + 1]
7
8            for j in range(len(w1)):
9                if j == len(w2):
10                    return False
11                
12                if w1[j] != w2[j]:
13                    if order_index[w1[j]] > order_index[w2[j]]:
14                        return False
15                    break
16        return True
class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        counts=0
        for i in range(0,30):
             if 1<<i&goal != 1<<i&start:
                 counts+=1
        return counts 

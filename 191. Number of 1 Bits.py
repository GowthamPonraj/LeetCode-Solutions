class Solution:
    def hammingWeight(self, n: int) -> int:
        
        counts=0
        while n!=0:
            n=n&(n-1)
            counts+=1

        return counts     

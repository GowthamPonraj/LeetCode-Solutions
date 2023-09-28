class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        counts=0
        while n>0:
            n=n&(n-1)
            counts+=1
        if counts==1:
            return True
        else:
            return False

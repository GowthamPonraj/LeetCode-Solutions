class Solution:
    def reverseBits(self, n: int) -> int:
       
        mask=1<<31
        ans=0
        for i in range(0,32):
            if mask&n==mask:
                ans=ans+2**i
            
            mask=mask>>1
        return ans

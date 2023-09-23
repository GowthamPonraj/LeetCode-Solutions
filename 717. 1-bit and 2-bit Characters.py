class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        if len(bits)==1 and bits[0]==0:
            return True
        i=0
        while i<len(bits):
            if bits[i]==1:
                i+=2
                ans=False
            else:
                i+=1
                ans=True
        return ans

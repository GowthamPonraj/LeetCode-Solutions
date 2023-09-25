class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        ans=0
        for i in range(len(nums)):
            counts=0
            j=i
            while i!=0:
                i=i&(i-1)
                counts+=1
            if counts==k:
                ans+=nums[j]
        return ans
            

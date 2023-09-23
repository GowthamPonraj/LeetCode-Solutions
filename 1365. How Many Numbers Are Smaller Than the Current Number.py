class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        lst=[]
        for i in range(0,len(nums)):
            counts=0
            for j in range(0,len(nums)):
                if i==j:
                    continue
                if nums[i]>nums[j]:
                    counts+=1
            lst.append(counts)
        return lst

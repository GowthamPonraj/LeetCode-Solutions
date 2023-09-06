class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        total=0
        ans=[]
        for i in accounts:
            for j in i:
                total+=j
            ans.append(total)
            total=0
        ans=sorted(ans)
        return ans[-1]

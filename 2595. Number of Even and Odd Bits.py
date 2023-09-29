class Solution:
    def evenOddBit(self, n: int) -> List[int]:
        values=[0,0]
        for i in range(0,10):
            if i%2==0:
                if n&(1<<i)== 1<<i:
                    values[0]+=1
            else:
                if n&(1<<i)==1<<i:
                    values[1]+=1
        return values
        

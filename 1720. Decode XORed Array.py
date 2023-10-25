class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        op=[first,]
        """ele=first
        for i in range(0,len(encoded)):
            j=0
            for j in range(0,100000):
                if encoded[i]==ele^j:
                    op.append(j)
                    ele=j
                    break
        return op"""
        for i in range(len(encoded)):
            op.append(op[i]^encoded[i])
        return op

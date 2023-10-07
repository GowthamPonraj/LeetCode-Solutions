class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        dct={}
        lst=[]
        for i in range(len(mat)):
            dct[i]=mat[i].count(1)
        dct=sorted(dct.items(),key=lambda x:x[1])
        for ky in range(k):
            lst.append(dct[ky][0])
        return lst

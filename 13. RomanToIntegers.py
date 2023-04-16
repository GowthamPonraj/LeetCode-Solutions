class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        dct={'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        totvalue=0
        ite=0
        for i in range(len(s)):
            if ite==1:
                ite=0
                continue
            
            ind=s[i]
            val=dct[ind]
            if i!=len(s)-1:
                nextind=s[i+1]
                nextval=dct[nextind]
            
          
            
                if nextval>val:
                    totvalue+=nextval-val
                    ite=1
                else:

                    totvalue+=val
                    ite=0
            else:
                totvalue+=val
                ite=0
    
        return totvalue

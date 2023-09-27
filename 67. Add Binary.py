class Solution:
    def addBinary(self, a: str, b: str) -> str:
        if a=="0" and b=="0":
            return "0"
        
        a=a.zfill(10000)
        b=b.zfill(10000)
        ans=""
        carry="0"
        for i in range(9999,-1,-1):
            lhs=a[i]+b[i]
            if (lhs=="10" or lhs=="01"):
                if carry=="0":
                    ans+="1"
                else:
                    ans+="0"
                    caryy="1"
            elif lhs=="00":
                if carry=="0":
                    ans+="0"
                else:
                    ans+="1"
                    carry="0"
            else:
                if carry=="1":
                    ans+="1"
                    carry="1"
                else:
                    ans+='0'
                    carry="1"
      
        if carry=="1":
            ans+="1"
        return (ans[::-1].lstrip("0"))

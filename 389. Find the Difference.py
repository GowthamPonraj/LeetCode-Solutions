class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if len(s)==0:
            return t
        ans=ord(t[len(t)-1])
        for i in range(len(s)):
            ans^=ord(s[i])^ord(t[i])
        return chr(ans)
        

class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransomNote=list(ransomNote)
        for i in magazine:
            if i in ransomNote:
                ransomNote.remove(i)
        if len(ransomNote)!=0:
            return False
        else:
            return True

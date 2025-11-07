class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        sour,tar = 0,0

        while sour<len(s) and tar<len(t):
            if s[sour] == t[tar]:
                sour +=1
            tar +=1
        return sour==len(s)
        
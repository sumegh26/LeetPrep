class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        target,source = 0,0

        while target<len(t) and source<len(s):
            if s[source]==t[target]:
                source +=1
            target +=1
        if source==len(s):
            return True
        else:
            return False       
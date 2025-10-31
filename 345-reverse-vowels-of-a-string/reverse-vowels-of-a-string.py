class Solution:
    def reverseVowels(self, s: str) -> str:
        vow = set("aeiouAEIOU")
        s_list = list(s)
        left,right = 0, len(s)-1
        while left<right:
            while left<right and s_list[left] not in vow:
                left +=1
            while left<right and s_list[right] not in vow:
                right -=1
            if left<right:
                s_list[left],s_list[right] = s_list[right],s_list[left]
                left +=1
                right -=1
        return "".join(s_list)
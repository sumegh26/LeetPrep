class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        freq_dic = {}
        count = 0
        for n in nums:
            compliment = k - n
            if freq_dic.get(compliment,0) > 0:
                count +=1
                freq_dic[compliment] -=1
            else:
                freq_dic[n] = freq_dic.get(n,0) + 1
        return count
        
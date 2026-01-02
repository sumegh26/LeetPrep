class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor = 0
        # for i in nums:
        #     xor ^= i
        # return xor
        HashMap = {}
        for i in nums:
            HashMap[i] = HashMap.get(i,0)+1
        for key,value in HashMap.items():
            if value==1:
                return key

        
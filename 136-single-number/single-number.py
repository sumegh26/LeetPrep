class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # xor = 0
        # for i in nums:
        #     xor ^= i
        # return xor
        HashMap = {}
        for i in nums:
            if i not in HashMap:
                HashMap[i] = 1
            else:
                HashMap[i] = 2
        for j in range(len(nums)):
            if HashMap[nums[j]]!=2:
                return nums[j]

        
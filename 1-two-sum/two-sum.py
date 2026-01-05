class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        mapp = {}
        for i in range(len(nums)):
            diff = target-nums[i]
            if diff in mapp:
                return [i,mapp[diff]]
            mapp[nums[i]]=i
         
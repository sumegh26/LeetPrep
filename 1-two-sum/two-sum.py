class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    return [i,j]
# A + B = C
# A - C = B
        mapper = {}
        for index,value in enumerate(nums):
            diff = target - value
            if diff in mapper:
                return [index, mapper[diff]]
            mapper[value] = index
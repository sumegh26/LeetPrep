class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # bruteforce, target, nums
        # for i in range(0,len(nums)):
        #     for j in range(i+1,len(nums)):
        #         if target == nums[i]+ nums[j]:
        #             return [i,j]
        # Hashmap
        mapperr = {}
        for i in range(0,len(nums)):
            comple_sum = target-nums[i]
            if comple_sum in mapperr:
                return [i,mapperr[comple_sum]]
            mapperr[nums[i]]=i
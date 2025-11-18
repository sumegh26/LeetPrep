class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        # result = []
        # for i in range(len(nums)):
        #     cnt = 0
        #     for j in range(len(nums)):
        #         if nums[i]>nums[j]:
        #             cnt += 1
        #     result.append(cnt)
        # return result
        sortedNums = sorted(nums)
        mappr = {}
        for index,value in enumerate(sortedNums):
            if value not in mappr:
                mappr[value] = index
        ret = []
        for i in nums:
            ret.append(mappr[i])
        return ret
                
            

        
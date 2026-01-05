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
        result = []
        mapp = {}
        sorted_nums = sorted(nums)
        for i in range(len(sorted_nums)):
            if sorted_nums[i] not in mapp:
                mapp[sorted_nums[i]] = i
        for i in nums:
            result.append(mapp.get(i))
        return result


                
            

        
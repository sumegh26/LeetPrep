class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # last_non_zero_index = 0
        # for i in range(len(nums)):
        #     if  nums[i]!= 0:
        #         nums[last_non_zero_index] = nums[i]
        #         last_non_zero_index +=1
        # for i in range(last_non_zero_index, len(nums)):
        #     nums[i] = 0
        l = 0
        for r in range(len(nums)):
            if nums[r]:
                nums[l],nums[r]=nums[r],nums[l]
                l +=1
        






        
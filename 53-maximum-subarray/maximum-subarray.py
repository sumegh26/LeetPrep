class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # ip = [-2,1,-3,4,1,2,1,-5,4]
        # op = 6 # [4,-1,2,1]

        curr_sum = 0
        max_sum = nums[0]

        for n in nums:
            if curr_sum < 0:
                curr_sum =0
            curr_sum += n
            max_sum = max(curr_sum,max_sum) 
        return max_sum

        
class Solution(object):
    def increasingTriplet(self, nums):
        first, second = float("inf"), float("inf")
        for i in range(len(nums)):
            if nums[i]<=first:
                first = nums[i]
            elif nums[i]<=second:
                second = nums[i]
            else:
                return True
        return False
        
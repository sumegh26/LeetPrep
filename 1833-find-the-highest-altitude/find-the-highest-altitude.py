class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height = 0
        curr_sum = 0
        for i in gain:
            curr_sum += i
            max_height = max(max_height, curr_sum)
        return max_height

        
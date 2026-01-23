class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_height =0
        curr_s =0
        for i in gain:
            curr_s += i
            max_height = max(max_height, curr_s)
        return max_height

        
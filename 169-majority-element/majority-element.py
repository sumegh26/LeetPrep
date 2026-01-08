class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        maj_map = {}
        max_ele = float('-inf')
        keyy = float('-inf')
        for i in nums:
            maj_map[i] = maj_map.get(i,0) + 1
        d = max(maj_map,key=maj_map.get)

        return d
        
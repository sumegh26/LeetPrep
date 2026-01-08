class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        result = []
        for n in nums1:
            if n in nums2:
                result.append(n)
        return list(set(result))
        
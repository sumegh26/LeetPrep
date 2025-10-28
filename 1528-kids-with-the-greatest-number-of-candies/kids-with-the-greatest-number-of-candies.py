class Solution(object):
    def kidsWithCandies(self, candies, extraCandies):
        """
        :type candies: List[int]
        :type extraCandies: int
        :rtype: List[bool]
        """
        ListResult = []
        maxCan = max(candies)
        for i in candies:
            if i+extraCandies >= maxCan:
                ListResult.append(True)
            else: ListResult.append(False)
        return ListResult
        
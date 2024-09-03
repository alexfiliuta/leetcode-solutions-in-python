class Solution(object):
    def rob(self, nums):
        last2 , last1 = 0 , 0
        for i in range(len(nums)):
            tempMax = max(last2 + nums[i], last1)
            last2 = last1
            last1 = tempMax
        return last1
        """
        :type nums: List[int]
        :rtype: int
        """
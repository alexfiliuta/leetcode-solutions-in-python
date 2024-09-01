class Solution(object):
    def canJump(self, nums):
        furthest = 0
        for x in range(len(nums)):
            if x > furthest:
                return False
            furthest = max(furthest, x+nums[x])
            if furthest >= len(nums)-1:
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
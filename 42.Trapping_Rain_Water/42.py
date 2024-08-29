class Solution(object):
    def trap(self, height):
        if not height:
            return 0
        res = 0
        l , r = 0 , len(height) - 1
        leftMax, rightMax = height[l], height[r]
        while l < r:
            if leftMax < rightMax:
                if height[l] < leftMax:
                    res += leftMax - height[l]
                l += 1
                leftMax = max(leftMax, height[l])
            else:
                if height[r] < rightMax:
                    res += rightMax - height[r]
                r -= 1
                rightMax = max(rightMax, height[r])
        return res
        """
        :type height: List[int]
        :rtype: int
        """
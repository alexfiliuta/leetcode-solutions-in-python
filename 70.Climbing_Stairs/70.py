class Solution(object):
    def __init__(self):
        self.memo = {}

    def climbStairs(self, n):
        if n in self.memo:
            return self.memo[n]
        elif n >= 2:
            self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2) 
            return self.memo[n]
        else:
            return 1
        """
        :type n: int
        :rtype: int
        """
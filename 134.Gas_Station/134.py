class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        if sum(gas) >= sum(cost):
            total = 0
            index = 0
            for i in range(len(gas)):
                total += (gas[i] - cost[i])
                if total < 0:
                    total , index = 0 , i+1
            return index
        else:
            return -1
            
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
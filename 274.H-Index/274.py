class Solution(object):
    def hIndex(self, citations):
        countSort = [0] * (len(citations)+1)
        for i in range(len(citations)):
            countSort[min(len(citations), citations[i] )] += 1

        res = 0
        for i in range(len(citations), -1, -1):
            res += countSort[i]
            if res >= i:
                return i
        return 0

        """
        :type citations: List[int]
        :rtype: int
        """
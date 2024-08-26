class Solution(object):
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        empty_rows = ['' for _ in range(numRows)]
        counter = 0
        going_down = False
        for char in s:
            empty_rows[counter] += char
            if counter == 0 or counter == numRows - 1:
                going_down = not going_down
            counter += 1 if going_down else -1 
        
        combined = ''.join(empty_rows)
        return combined
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
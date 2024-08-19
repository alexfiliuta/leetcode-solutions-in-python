class Solution(object):
    def strStr(self, haystack, needle):
        i , j = 1 , 0
        prefix_table = [-1] + [0] * len(needle)

        while i < len(needle):
            if j == -1 or needle[i] == needle[j]:
                i += 1
                j += 1
                prefix_table[i] = j
            else:
                j = prefix_table[j]
        
        i , j = 0 , 0
    
        while i < len(haystack) and j < len(needle):
            if j == -1 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = prefix_table[j]
        if j == len(needle):
            return i-j
        else:
            return -1
        
        """ 
        :type haystack: str
        :type needle: str
        :rtype: int
        """


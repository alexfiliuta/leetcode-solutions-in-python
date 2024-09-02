class Solution(object):
    def reverseWords(self, s):
        left , right , current = 0 , 0 , 0
        s = s[::-1]
        words = s.split()

        return ' '.join(word[::-1] for word in words)
        """
        :type s: str
        :rtype: str
        """
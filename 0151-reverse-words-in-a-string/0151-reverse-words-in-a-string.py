class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        # with the help of inbuilt function
        words = s.strip().split()
        reversed_word = words[::-1]
        return ' '.join(reversed_word)
# https://leetcode.com/problems/reverse-words-in-a-string/description/

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new_s = s.split()
        new_s.reverse()
        return " ".join(new_s)
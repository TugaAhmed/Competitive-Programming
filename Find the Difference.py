# https://leetcode.com/problems/find-the-difference/

class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        for char1 , char2 in zip(sorted(s) , sorted(t)):
            if char1 != char2 :
                return char2
        else :
            return sorted(t)[len(sorted(t)) - 1]
        
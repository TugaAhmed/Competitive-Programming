class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        start = False 
        i = len(s) - 1 
        while i >= 0 :
            if start and s[i] == " " :
                break
            elif s[i] != " " and not start :
                start = i

            i -= 1

        return start - i 
# https://leetcode.com/problems/decrypt-string-from-alphabet-to-integer-mapping/description/


class Solution(object):
    def freqAlphabets(self, s):
        """
        :type s: str
        :rtype: str
        """
        mapping_s = "abcdefghijklmnopqrstuvwxyz"
        answer = "" 
        index = 0
        while index <= len(s) - 1 :
            if '#' in s[index:index+3] : # from j to z
                answer += mapping_s[int(s[index:index+2]) - 1 ] 
                index += 3
            else :  # from a to i 
                answer += mapping_s[int(s[index]) - 1 ] 
                index += 1 
        
        return answer
            


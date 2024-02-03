# https://leetcode.com/problems/longest-common-prefix/description/


class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """
        longest_prefix = ""
        strs.sort()
        for i , letter in enumerate(strs[0]) : # for each letter 
            if all(word[i] == letter for word in strs[1:]):
                longest_prefix += letter
            else:
                break
        
        return longest_prefix
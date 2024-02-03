# https://leetcode.com/problems/merge-strings-alternately/description/


class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        output = ""
        extra = ""
        longer_word = word1
        if len(word1) != len(word2) :
            longer_word = word1 if len(word1) > len(word2) else word2
            extra = longer_word[-1 * (abs(len(word1) - len(word2))) : ]
        for i in range(len(longer_word) - len(extra)) :
            output += word1[i] + word2[i]
        output += extra

        return output
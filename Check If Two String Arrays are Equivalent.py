# https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/description/

class Solution(object):
    def arrayStringsAreEqual(self, word1, word2):
        """
        :type word1: List[str]
        :type word2: List[str]
        :rtype: bool
        """

        word_1 = ""
        word_2 = ""

        for i in word1 :
            word_1 += i 
        
        for i in word2 :
            word_2 += i 
        
        if word_1 == word_2 :
            return True 
        
        return False
        
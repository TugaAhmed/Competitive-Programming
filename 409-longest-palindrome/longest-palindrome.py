from collections import Counter 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count_dict = Counter(s)
        ans =  0
        odd_added = False
        for val in count_dict.values() :
            if val % 2 == 0 : 
                ans += val 
            else : 
                ans += val - 1 
            
            if val % 2 != 0 and not odd_added :
                ans += 1 
                odd_added = True 
        
        return ans 
            

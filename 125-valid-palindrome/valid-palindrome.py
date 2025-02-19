class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        s = [i.lower() for i in s if i.isalpha() or i.isnumeric() ]
        
        i = 0 
        j = len(s) - 1 

        while i < j : 
            if s[i] == s[j] :
                i += 1 
                j -= 1 
            else :
                return False 
        return True
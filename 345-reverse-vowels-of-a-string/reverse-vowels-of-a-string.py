class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """

        i = 0 
        j = len(s)-1
        s = list(s)
        vowels = ['a','e','i','o','A','E','I','O','u','U']

        while i < j : 
            if s[i] in vowels : 
                while s[j] not in vowels : 
                    j -= 1 
                # print("i",i,'j',j,'s',s)
                # Swap characters
                s[i], s[j] = s[j], s[i]
                i += 1
                j -= 1 
                
            else :   
                i += 1 
        
        s = "".join(s)
        return s 

        
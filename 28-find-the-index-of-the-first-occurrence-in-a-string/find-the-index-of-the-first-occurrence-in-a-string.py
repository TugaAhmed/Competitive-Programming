class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if needle not in haystack :
            return -1 
        
        else : 
            i = 0
            index = 0 
            main_index = 0
            while index < len(haystack) :
                letter = haystack[index]
                if needle[i] == letter :            
                    if i == len(needle) - 1 : 
                        return index - (len(needle) - 1)
                        break 
                    i += 1
                else : 
                    i = 0 
                    index = main_index
                    main_index += 1 

                index += 1
                    
        
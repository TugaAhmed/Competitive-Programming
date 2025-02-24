from collections import Counter
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """

        count_dict = Counter(magazine)

        for letter in ransomNote : 
            if count_dict[letter] > 0 :
                count_dict[letter] -= 1 
            else :
                return False

        return True 

        
        
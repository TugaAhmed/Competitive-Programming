from collections import defaultdict
class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        map_dict1 = defaultdict(int)
        map_dict2 = defaultdict(int)
        s = s.split()
        
        if len(s) != len(pattern) :
            return False

        for i in range(len(pattern)) :
            if not map_dict1[pattern[i]] : 
                if map_dict2[s[i]] :
                    return False
                map_dict1[pattern[i]] = s[i]
                map_dict2[s[i]] = pattern[i]
            elif map_dict1[pattern[i]] != s[i] :
                return False 

        return True 
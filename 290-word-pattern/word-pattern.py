class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        
        map_dict = {}
        s = s.split()
        mapped = []
        if len(s) != len(pattern) :
            return False

        for i in range(len(pattern)) :
            if pattern[i] not in map_dict : 
                if s[i] in mapped :
                    return False
                map_dict[pattern[i]] = s[i]
                mapped.append(s[i])
            elif pattern[i] in map_dict and map_dict[pattern[i]] != s[i] :
                return False 

        return True 
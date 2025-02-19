class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        map_dict = {}
        mapped = []
        for i in range(len(s)) :
            if s[i] not in map_dict : 
                if t[i] not in mapped :
                    map_dict[s[i]] = t[i]
                    mapped.append(t[i])
                else : 
                    return False 
            elif s[i] in map_dict and map_dict[s[i]] != t[i] :
                return False 
            
        return True 
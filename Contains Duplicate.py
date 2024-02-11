# https://leetcode.com/problems/contains-duplicate/description/

class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        seen_set = set()
        for num in nums :
            if num in seen_set :
                return True 
            seen_set.add(num)
        return False

        
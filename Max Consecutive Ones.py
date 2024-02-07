# https://leetcode.com/problems/max-consecutive-ones/

class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_con = 0 
        count = 0
        for i in nums :
            if i == 1 :
                count += 1 
            else :
                count = 0
            if count > max_con:
                max_con = count 
        return max_con
        
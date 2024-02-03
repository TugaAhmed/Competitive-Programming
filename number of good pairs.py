# https://leetcode.com/problems/number-of-good-pairs/description/

class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        good_pairs = 0
        count_dict = {}
        for num in nums:
            if num in count_dict:
                good_pairs += count_dict[num] 
                count_dict[num] += 1  
            else:
                count_dict[num] = 1  

        return good_pairs
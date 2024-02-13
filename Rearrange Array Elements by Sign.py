# https://leetcode.com/problems/rearrange-array-elements-by-sign/description/

class Solution(object):
    def rearrangeArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        
        positive_nums = [num for num in nums if num >= 0 ]
        negative_nums = [num for num in nums if num < 0]

        return [num for pair in zip(positive_nums, negative_nums) for num in pair]
# https://leetcode.com/problems/shuffle-the-array/description/


class Solution(object):
    def shuffle(self, nums, n):
        """
        :type nums: List[int]
        :type n: int
        :rtype: List[int]
        """
        final_list = []

        [final_list.extend([nums[i], nums[i + n]]) for i in range(len(nums)) if i < n]
        
        return final_list
        
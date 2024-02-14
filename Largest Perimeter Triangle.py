# https://leetcode.com/problems/largest-perimeter-triangle/description/

class Solution(object):
    def largestPerimeter(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        sorted_nums = sorted(nums)
        i = len(nums) - 1


        while i >= 2 :
            if sorted_nums[i-1] + sorted_nums[i-2] > sorted_nums[i] :
                return sorted_nums[i-1] + sorted_nums[i-2] + sorted_nums[i]
            i -= 1
        
        return 0


        
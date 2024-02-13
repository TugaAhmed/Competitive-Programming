# https://leetcode.com/problems/partition-array-according-to-given-pivot/description/

class Solution(object):
    def pivotArray(self, nums, pivot):
        """
        :type nums: List[int]
        :type pivot: int
        :rtype: List[int]
        """

        befor_pivot = [num for num in nums if num < pivot]
        equal_pivot = [num for num in nums if num == pivot]
        after_pivot = [num for num in nums if num > pivot]
        
        return befor_pivot + equal_pivot + after_pivot
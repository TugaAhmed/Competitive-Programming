# https://leetcode.com/problems/replace-elements-in-an-array/ 

class Solution(object):
    def arrayChange(self, nums, operations):
        """
        :type nums: List[int]
        :type operations: List[List[int]]
        :rtype: List[int]
        """
        answer = [0] * len(nums)

        nums_dict = {}
        for i in range(len(nums)) :
            nums_dict[nums[i]] = i
        
        for operation in operations : 
            nums_dict[operation[1]] = nums_dict[operation[0]]
            del nums_dict[operation[0]]

        for key , value in nums_dict.items() :
            answer[value] = key

        return answer

        
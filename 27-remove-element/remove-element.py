class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        
        occur = nums.count(val)
        i = 0 
        while i < len(nums):
            if nums[i] == val :
                nums.remove(val)
                nums.append('_')
            else :
                i += 1
        return len(nums) - occur

       
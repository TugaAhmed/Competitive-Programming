class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        current = -101 
        k = 0 
        i = 0
        nums_len = len(nums)
        while i < nums_len :
            num = nums[i]
            if num != current : 
                current = num 
                i += 1 
                if current == '_':
                    break
            else : 
                k += 1 
                nums.remove(num)
                nums.append('_')

        return nums_len-k 
# https://leetcode.com/problems/majority-element-ii/description/?envType=daily-question&envId=2023-10-05

class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """

        count_dict = {}
        majority = len(nums) / 3
        answer = []

        for num in nums :
            if num in count_dict :
                count_dict[num] += 1 
            else :
                count_dict[num] = 1
        
        for key,value in count_dict.items() :
            if value > majority :
                answer.append(key)

        return answer


        
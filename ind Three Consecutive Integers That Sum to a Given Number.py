# https://leetcode.com/problems/find-three-consecutive-integers-that-sum-to-a-given-number/submissions/1168302659/

class Solution(object):
    def sumOfThree(self, num):
        """
        :type num: int
        :rtype: List[int]
        """

        mid_num = num / 3 
        if num % 3 != 0 :
            return []
        else :
            return [mid_num-1 , mid_num , mid_num +1] 
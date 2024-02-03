# https://leetcode.com/problems/smallest-even-multiple/

class Solution(object):
    def smallestEvenMultiple(self, n):
        """
        :type n: int
        :rtype: int
        """        
        new_n = n
        smallest_positive = 0
        while smallest_positive == 0  :
            if new_n % n == 0 and new_n % 2 == 0 :
                smallest_positive = new_n
            else :
                new_n += 1 

        return smallest_positive 
from collections import Counter 
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        count_dict = Counter(s)

        even_sum = sum(i for i in count_dict.values() if i%2 == 0 )
        odd_vals = [i-1 for i in count_dict.values() if i%2 != 0 ]
        
        if odd_vals :
            return (sum(odd_vals) + even_sum) + 1 
        return even_sum

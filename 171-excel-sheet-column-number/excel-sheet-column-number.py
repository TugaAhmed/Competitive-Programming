class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        ans = 0 
        index = len(columnTitle)
        counter = 26 ** (index-1)

        for letter in columnTitle : 
            ans += counter * (ord(letter)-64)
            index -= 1 
            counter /= 26

        return ans
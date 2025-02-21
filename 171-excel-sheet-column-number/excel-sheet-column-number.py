class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """

        ans = 0 
        index = len(columnTitle)


        for letter in columnTitle : 
            ans += (26)**(index-1) * (ord(letter)-64)
            index -= 1 

        return ans
class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        

        current_d = columnNumber // 26
        current_r = columnNumber % 26 
        ans = ""
        
        while current_d > 0 : 
            if current_r == 0 :
                current_r = 26
                current_d -= 1 
                ans += chr(current_r+64)
            else :
                ans += chr(current_r+64)
            current_r = current_d %  26
            current_d = current_d // 26 

        if current_r :
            ans += chr(current_r+64)
        return ans[::-1]
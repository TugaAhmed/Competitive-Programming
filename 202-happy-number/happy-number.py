class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        
        power_dict = {'0':0 , '1':1 , '2' :4 , '3':9 , '4' :16 , '5':25 ,
                      '6':36  , '7':49 , '8':64 , '9':81}

        ans = 0 
        for i in range(100) :
            old_n = str(n)
            # print("list",[power_dict[old_n[i]] for i in range(len(old_n))])
            ans = sum([power_dict[old_n[i]] for i in range(len(old_n))])
            # print("ans",ans)
            if ans == 1 :
                return True 
            n = int(ans) 
            # print("n",n) 
        
        return False
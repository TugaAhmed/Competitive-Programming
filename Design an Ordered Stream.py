# https://leetcode.com/problems/design-an-ordered-stream/description/

class OrderedStream(object):

    def __init__(self, n):
        """
        :type n: int
        """
        self.n = n 
        self.stream_list = [""] * n 
        self.pointer = 0 

    def insert(self, idKey, value):
        """
        :type idKey: int
        :type value: str
        :rtype: List[str]
        """
        result = []
        self.stream_list[idKey-1] = str(value) 
        if self.stream_list[self.pointer] != "" : 
            for item in self.stream_list[self.pointer:]  : 
                if item != "" :
                    result.append(item)
                    self.pointer += 1 
                else :
                    break
        return result
    

# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
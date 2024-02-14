# https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/

class Solution(object):
    def minOperations(self, boxes):
        """
        :type boxes: str
        :rtype: List[int]
        """
        answer = []
        balls_positions = [index for index,value in enumerate(boxes) if value == '1' ]
        
        for index , value in enumerate(boxes) :
            answer.append( sum([abs(index - ball_position) for ball_position in balls_positions 
            if index != ball_position]) )
        
        return answer
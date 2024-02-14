# https://leetcode.com/problems/escape-the-ghosts/description/
class Solution(object):
    def escapeGhosts(self, ghosts, target):
        """
        :type ghosts: List[List[int]]
        :type target: List[int]
        :rtype: bool
        """

        user_target_distance = abs(target[0]) + abs(target[1])

        for ghost in ghosts :
            ghost_target_distance = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])
            if ghost_target_distance <= user_target_distance :
                return False
        
        return True 
        
# https://leetcode.com/problems/card-flipping-game/submissions/

class Solution(object):
    def flipgame(self, fronts, backs):
        """
        :type fronts: List[int]
        :type backs: List[int]
        :rtype: int
        """
        visited=set()
        dublicate=set()
        for front,back in zip(fronts,backs):
            visited.add(front)
            visited.add(back)
            if front == back:
                dublicate.add(front)
        return min(visited-dublicate) if(visited-dublicate) else 0 
        
        

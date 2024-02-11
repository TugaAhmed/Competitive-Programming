# https://leetcode.com/problems/find-players-with-zero-or-one-losses/description/

class Solution(object):
    def findWinners(self, matches):
        """
        :type matches: List[List[int]]
        :rtype: List[List[int]]
        """
        answer = [[] , []]
        lose_frequency = {}  #
        for match in matches :
            if match[1] in lose_frequency  :
                lose_frequency[match[1]] += 1
            else :
                lose_frequency[match[1]] = 1
            
            if match[0] not in lose_frequency :
                lose_frequency[match[0]] = 0
        
        for key,value in lose_frequency.items() :
            if value == 0 :
                answer[0].append(key)
            if value == 1 :
                answer[1].append(key)
            
        answer[0].sort()
        answer[1].sort()
        return answer

            
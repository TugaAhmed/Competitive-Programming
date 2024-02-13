# https://leetcode.com/problems/minimum-index-sum-of-two-lists/description/

class Solution(object):
    def findRestaurant(self, list1, list2):
        """
        :type list1: List[str]
        :type list2: List[str]
        :rtype: List[str]
        """

        common_strings_dict = {}
        min_index_sum = 0
        shorter_list = list1 if len(list1) <= len(list2) else list2
        longer_list = list1 if len(list1) > len(list2) else list2

        for index , value in enumerate(shorter_list) :
            if value in longer_list :
                common_strings_dict[value] = index + longer_list.index(value)
        
        min_index_sum = min(common_strings_dict.values())

        return [key for key, value in common_strings_dict.items() if value == min_index_sum]
        

        
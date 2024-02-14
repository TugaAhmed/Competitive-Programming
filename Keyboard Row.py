# https://leetcode.com/problems/keyboard-row/description/

class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """

        keyboard_rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        answer = []

        for word in words:
            if all(letter.lower() in keyboard_rows[0] for letter in word):
                answer.append(word)
            elif all(letter.lower() in keyboard_rows[1] for letter in word):
                answer.append(word)
            elif all(letter.lower() in keyboard_rows[2] for letter in word):
                answer.append(word)

        return answer

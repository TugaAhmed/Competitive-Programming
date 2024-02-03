# https://leetcode.com/problems/convert-the-temperature/description/

class Solution(object):
    def convertTemperature(self, celsius):
        """
        :type celsius: float
        :rtype: List[float]
        """
        kelvin = round(celsius + 273.15, 5)
        fahrenheit = round(celsius * 1.80 + 32.00, 5)
        array = [kelvin, fahrenheit]

        return array 
        
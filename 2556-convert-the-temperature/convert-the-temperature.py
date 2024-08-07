class Solution:
    def convertTemperature(self, celsius: float) -> List[float]:
        lst=[]
        lst.append(celsius + 273.15)
        lst.append(celsius * 1.80 + 32.00)
        return lst
        
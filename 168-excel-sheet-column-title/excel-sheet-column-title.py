class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        result = ""
        while columnNumber > 0:
            remainder = (columnNumber - 1) % 26  # Convert 1-based to 0-based index
            result = chr(65 + remainder) + result  # Convert remainder to corresponding letter
            columnNumber = (columnNumber - 1) // 26  # Update column number for next iteration
        return result

            




        
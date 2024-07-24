class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        title = ""
        while columnNumber > 0:
            columnNumber-=1
            title = chr(columnNumber % 26 +65) + title
            columnNumber = columnNumber//26
        return title
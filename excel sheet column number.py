# Given a string columnTitle that represents the column title as appear in an Excel sheet, return its corresponding column number.

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        dic=dict(zip(string.ascii_uppercase,(i for i in range(1,27))))
        num=0
        for ch in columnTitle:
            num=26*num+dic[ch]
        return num
            
            
            
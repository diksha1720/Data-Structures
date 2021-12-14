class Solution:
    def convertToTitle(self, columnNumber: int) -> str: 
        
        if columnNumber==0:
            return ''
        
        q,r=divmod(columnNumber-1,26)
        
        return self.convertToTitle(q)+chr(r+ord('A'))
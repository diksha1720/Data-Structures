class Solution:
    def addBinary(self, a: str, b: str) -> str:
        sum_=(int(a,2)+int(b,2))
        res="{0:b}".format(sum_)
        return (res)

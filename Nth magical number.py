# A positive integer is magical if it is divisible by either a or b.

# Given the three integers n, a, and b, return the nth magical number. Since the answer may be very large, return it modulo 109 + 7.

class Solution:
    def nthMagicalNumber(self, n: int, a: int, b: int) -> int:
        ab = lcm(a,b)
        lo, hi = 0, n*min(a, b)
        while lo < hi: 
            mid = lo + hi >> 1
            if mid//a + mid//b - mid//ab < n: lo = mid + 1
            else: hi = mid 
        return lo % 1_000_000_007
        # if a==b:
        #     return (a*n)%1000000007
        # x=min(a,b)
        # y=max(a,b)
        # # print(x)
        # # print(y)
        # res=set()
        # for i in range(1,n+1):
        #     res.add(x*i)
        #     res.add(y*i)       
        # fin=list(res)
        # fin.sort()
        # # print(fin)
        # ans=fin[n-1]%(1000000007)
        # return ans
            
        
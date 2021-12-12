# An ugly number is a positive integer whose prime factors are limited to 2, 3, and 5.

# Given an integer n, return the nth ugly number.

 

class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        
        p2,p3,p5=0,0,0
        
        for i in range(n+1):
            t2=dp[p2]*2
            t3=dp[p3]*3
            t5=dp[p5]*5
            
            temp=min(t2,t3,t5)
            
            dp.append(temp)
            
            if temp==dp[p2]*2:
                p2+=1
            if temp==dp[p3]*3:
                p3+=1
            if temp==dp[p5]*5:
                p5+=1
        # print(dp)        
        return dp[n-1]
        
        
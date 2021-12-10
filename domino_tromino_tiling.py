# You have two types of tiles: a 2 x 1 domino shape and a tromino shape. You may rotate these shapes.


# Given an integer n, return the number of ways to tile an 2 x n board. Since the answer may be very large, return it modulo 109 + 7.

# In a tiling, every square must be covered by a tile. Two tilings are different if and only if there are two 4-directionally adjacent cells on the board such that exactly one of the tilings has both squares occupied by a tile.

class Solution:
    def numTilings(self, n: int) -> int:
        if n<=2:
            return n
        mod=10**9+7
        dp=[0]*(n+1)
        dp[0]=1
        dp[1]=1
        dp[2]=2
        Sum=dp[0]
        for i in range(3,n+1):
            dp[i]=dp[i-1]+dp[i-2]+2*Sum
            Sum+=dp[i-2]
            dp[i]%=mod
        return dp[n]
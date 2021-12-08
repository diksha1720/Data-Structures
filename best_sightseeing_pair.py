# You are given an integer array values where values[i] represents the value of the ith sightseeing spot. Two sightseeing spots i and j have a distance j - i between them.

# The score of a pair (i < j) of sightseeing spots is values[i] + values[j] + i - j: the sum of the values of the sightseeing spots, minus the distance between them.

# Return the maximum score of a pair of sightseeing spots.

class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        n=len(values)
        dp=[0]*n
        dp[0]=values[0]
        maxval=0
        for i in range(1,n):
            dp[i]=max(dp[i-1],values[i-1]+i-1)
            # print(dp)
            maxval=max(maxval,dp[i]+values[i]-i)
        return maxval
  
# Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

# Note that the same word in the dictionary may be reused multiple times in the segmentation.

 
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
   
   
        n=len(s)
        dp = [False for _ in range(n+1)]
        dp[0]=True
    
    
    
        for i in range(n):
            if dp[i]:
                for w in wordDict:
                    if s[i:i+len(w)]==w:
                        dp[i+len(w)]=True
        return dp[-1]
        

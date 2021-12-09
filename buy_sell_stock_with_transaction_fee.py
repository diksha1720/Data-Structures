# You are given an array prices where prices[i] is the price of a given stock on the ith day, and an integer fee representing a transaction fee.

# Find the maximum profit you can achieve. You may complete as many transactions as you like, but you need to pay the transaction fee for each transaction.

# Note: You may not engage in multiple transactions simultaneously (i.e., you must sell the stock before you buy again).

 

class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
       
        cin_w_shares = -prices[0] 
        cin_wo_shares = 0 
        
        for i in range(1,len(prices)):
           
            cin_w_shares = max(cin_w_shares, cin_wo_shares-prices[i]) 
            
           
            cin_wo_shares = max(cin_wo_shares, cin_w_shares + prices[i]-fee)
            
       
        return cin_wo_shares 
        
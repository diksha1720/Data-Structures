# You are given an array prices where prices[i] is the price of a given stock on the ith day.

# You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

# Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.
class Solution:
    def maxProfit(self, price: List[int]) -> int:
        min_so_far=100000000
        max_sum=0
        for num in price:
            if num<min_so_far:
                min_so_far=num
                continue
            else:
                max_sum=max(max_sum,num-min_so_far)
        return max_sum
        
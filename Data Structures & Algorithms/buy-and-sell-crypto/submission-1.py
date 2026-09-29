class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        lowest_price = prices[0]
        largest_profit = 0

        for price in prices:
            if price < lowest_price:
                lowest_price = price
            else:
                cur_sell_price = price - lowest_price
                largest_profit = max(largest_profit, cur_sell_price)
        return largest_profit        
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit= 0
        min_price = prices[0]

        for price in prices:
            if price < min_price:
                min_price = price

            profit= price - min_price
            max_profit = max(max_profit, profit)

        return max_profit


prices = [7,1,5,3,6,4]
solution = Solution()
print(solution.maxProfit(prices))
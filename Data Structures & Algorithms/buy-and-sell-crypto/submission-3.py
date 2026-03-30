class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        output = 0
        l = 0

        for r in range(len(prices)):
            curr = prices[r] - prices[l]
            output = max(output, curr)

            if prices[r] < prices[l]:
                l = r

        return output
            



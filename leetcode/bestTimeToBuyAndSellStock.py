class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max = 0
        min = 9999999999999999999999999
        for i in range(len(prices)):
            if prices[i] < min:
                min = prices[i]
            elif prices[i] - min > max:
                max = prices[i] - min
        return max

    def naiveBruteForceSolution(self, prices):
        output = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                transaction = prices[j] - prices[i]
                if transaction > output:
                    output = transaction
        return output

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #   运行超时
        # if prices == sorted(prices):
        #     return prices[-1] - prices[0]
        # elif prices == sorted(prices, reverse=True):
        #     return 0
        # else:
        #     p = []
        #     # tem = prices
        #     tem = []
        #     while prices:
        #         index_min = prices.index(min(prices))
        #         tem = prices[index_min:]
        #         p.append(max(tem) - tem[0])
        #         prices.pop(index_min)
        #     return max(p)

        # method 2
        # min_p = 99999999999
        # max_p = 0
        # for i in range(len(prices)):
        #     min_p = min(min_p, prices[i])
        #     max_p = max(max_p, prices[i] - min_p)
        # return max_p
        # method 3
        if len(prices) == 0:
            return 0
        min_p = prices[0]
        max_p = 0
        for i in prices:
            if i < min_p:
                min_p = i
            if i - min_p > max_p:
                max_p = i - max_p
        return max_p
s = Solution()
p = [7,1,5,3,6,4]
print(s.maxProfit(p))



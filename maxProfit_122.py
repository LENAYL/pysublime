class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        #  method  1
        # sum = 0
        # min_p = 2**31
        # for i in prices:
        #     if i < min_p:
        #         min_p = i
        #     else:
        #         sum = sum + i - min_p
        #         min_p = i
        # return sum



        # method 2
        sum = 0
        if len(prices) < 2:
            return 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices[i]:
                sum += prices[i+1] - prices[i]
        return sum
s = Solution()
p = [7,1,5,3,10,6,4]
print(s.maxProfit(p))

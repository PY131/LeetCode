# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/best-time-to-buy-and-sell-stock/

@Problem:
    Say you have an array for which the ith element is the price of a given stock on day i.

    If you were only permitted to complete at most one transaction 
    (i.e., buy one and sell one share of the stock), 
    design an algorithm to find the maximum profit.

    Note that you cannot sell a stock before you buy one.

Example 1:
    Input: [7,1,5,3,6,4]
    Output: 5
    Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
                 Not 7-1 = 6, as selling price needs to be larger than buying price.
Example 2:
    Input: [7,6,4,3,1]
    Output: 0
    Explanation: In this case, no transaction is done, i.e. max profit = 0.
"""

class Solution(object):

    def maxProfit(self, prices):
        """
        from the states transform func in maxProfit_v2, we can see that dp[i+1] only depends on dp[i]
        so we do not need to store all DP table
        and the space cost can reduce to O(1)
        """
        N = len(prices)
        dp_0 = 0
        dp_1 = float('-inf')
        for i in range(N):
            dp_0 = max(dp_0, dp_1 + prices[i])
            dp_1 = max(dp_1, -prices[i])  # dp_1 = max(dp_1, dp_0 - prices[i]) as dp_0 is 0 as transaction times limit K=1
        return dp_0

    def maxProfit_v2(self, prices):
        """
        :method: using DP
        :dp[i][k][j]: max profit
            i~[0: n): the i-th day
            k~[0: K]: K=max transaction times left, here is 1 initially, while buying, k-1
            j~[0, 1]: 0=not-have, 1=have stock
            :states transform:
                dp[i][k][0] = max(dp[i-1][k][0], dp[i-1][k][1] + prices[i])
                dp[i][k][1] = max(dp[i-1][k][1], dp[i-1][k-1][0] - prices[i])  # buy it today and the max transaction time left is 0 at day i-1
            :base case:
                dp[-1][xx][0] = 0  # as time is invalid
                dp[xx][0][0] = 0  # as no transaction is allowed
                dp[-1][xx][1] = -inf  # impossible
                dp[xx][0][1] = -inf  # impossible
            :here we can see that states transform 
        :Complexity:
            time: O(n)
            space: O(N*K*S)
        """
        N = len(prices)
        K = 2
        S = 2
        dp = [[[float("-inf") if ((i == 0 or k == 0) and j == 1) else 0 for j in range(S)] for k in range(K)] for i in range(N+1)]
        # states transform
        for i in range(N):
            dp[i+1][1][0] = max(dp[i][1][0], dp[i][1][1] + prices[i])
            dp[i+1][1][1] = max(dp[i][1][1], dp[i][0][0] - prices[i])
            print i+1, dp[i+1][1]
        return dp[N][1][0]

    def maxProfit_v1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :method:
            iterate once: i~0->n, recording the smallest up to current index, 
            get the max between all prices[i] - smallest
        :complexity:
            time: O(n)
            space: O(1)
        """
        if not prices:
            return 0
        res = 0
        smallest = prices[0]
        for cur in prices[1:]:
            if res < cur - smallest:
                res = cur - smallest
            elif cur < smallest:
                smallest = cur
        return res

    def maxProfit_v0(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        :method:
            using two iterative: i~0->n and j~i->n, find the max prices[j]-prices[i]
        :complexity:
            time: O(n^2)
            space: O(1)
        """
        res = 0
        n = len(prices)
        for i in range(n):
            num_i = prices[i]
            num_j = max(prices[i:])
            if res < num_j - num_i:
                res = num_j - num_i
        return res

if __name__ == "__main__":
    so = Solution()
    arr = [7,1,5,3,6,4]
    # arr = [2,1,3]
    res = so.maxProfit(arr)
    print res

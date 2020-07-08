# coding: utf8
# python 2.7
class Solution(object):
    def maxProfit(self, k, prices):
        """
        :type k: int
        :type prices: List[int]
        :rtype: int
        """
        n = len(prices)
        if n == 0 or k == 0:
            return

        dp = [[[0 for _ in range(2)] for _ in range(k+1)] for _ in range(n)]

        for i in range(n):
            for j in range(k+1):
                if i == 0 or j == 0:
                    dp[i][j][0] = 0
                    dp[i][j][1] = float("-inf") if j == 0 else -prices[i]
                else:
                    dp[i][j][0] = max(dp[i-1][j][0], dp[i-1][j][1] + prices[i])
                    dp[i][j][1] = max(dp[i-1][j][1], dp[i-1][j-1][0] - prices[i])
        return max([x[0] for x in dp[n-1]])

if __name__ == "__main__":
    so = Solution()
    arr = [3,2,6,5,0,3]
    k = 2
    res = so.maxProfit(k, arr)
    print res

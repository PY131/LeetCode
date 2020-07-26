# coding: utf8
# python 2.7

class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i-1]]
        return dp[amount]

if __name__ == "__main__":
    obj = Solution()
    res = obj.change(coins = [1, 2, 5], amount = 5)
    print res

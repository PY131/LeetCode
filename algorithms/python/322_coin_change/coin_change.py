# coding: utf8
# python 2.7
"""
You are given coins of different denominations and a total amount of money amount. 
Write a function to compute the fewest number of coins that you need to make up that amount. 
If that amount of money cannot be made up by any combination of the coins, return -1.

Example 1:
    Input: coins = [1, 2, 5], amount = 11
    Output: 3 
    Explanation: 11 = 5 + 5 + 1
Example 2:

    Input: coins = [2], amount = 3
    Output: -1
Note:
    You may assume that you have an infinite number of each kind of coin.

Link: https://leetcode-cn.com/problems/coin-change
"""

class Solution(object):
    def coinChange(self, coins, amount):
        """
        :type coins: List[int]
        :type amount: int
        :rtype: int
        :idea: using DP, time: O(n), space: O(n)
        """
        S = [-1] * (amount + 1)
        S[0] = 0
        for i in range(1, amount + 1):
            pre_min = -1
            for c in coins: 
                if i - c < 0 or S[i - c] < 0:
                    continue
                if pre_min >= 0 and pre_min < S[i - c]:
                    continue
                pre_min = S[i - c]
            if pre_min >= 0:
                S[i] = pre_min + 1
        return S[amount]

if __name__ == '__main__':
    so = Solution()
    coins = [2,5,10,1]
    amount = 27
    res = so.coinChange(coins, amount)
    print res

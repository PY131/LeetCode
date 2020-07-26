# -*- coding: utf-8 -*-

class Knapsack(object):

    def zero_one_pack(self, v, c, w):
        '''
        we have set S contains n items, each‘s volumn is ci, and worths of wi
        we have a backpack with max volumn of v
        now our problem is, how to put the items into our backpack and get the max sum of worth
        params:
            c = [c1, c2, ..., c_n-1]
            w = [w1, w2, ..., w_n-1]
            v = v
        '''
        # assert len(c) = len(w)
        n = len(c)
        # to solve this, we define m[i][j] means util i-th item be choosed, with the sum_volumn <= j, the max value we get
        # i ～ [0, n], j ~ [0, v]
        dp = [ [0 for _ in range(v+1)] for _ in range(n+1)]
        for i in range(1, n+1):
            for j in range(1, v+1):
                if c[i-1] > j:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = max(dp[i-1][j], dp[i-1][j-c[i-1]] + w[i-1])
        return dp[n][v]

    def zero_one_pack_v2(self, v, c, w):
        n = len(c)
        dp = [0] * (v+1)
        for i in range(1, n+1):
            for j in range(v, 0, -1):
                if c[i-1] <= j:
                    dp[j] = max(dp[j], dp[j-c[i-1]] + w[i-1])
        return dp[v]

    def zero_one_pack_v3(self, v, c, w):
        # what if we need full backpack exactly, where sum of the choosed ci equals to v
        n = len(c)
        dp = [float("-inf")] * (v+1)
        dp[0] = 0
        for i in range(1, n+1):
            for j in range(v, 0, -1):
                if c[i-1] <= j:
                    dp[j] = max(dp[j], dp[j-c[i-1]] + w[i-1])
            print dp
        return dp[v]

    def complete_pack(self, v, c, w):
        # each kind of item has unlimited number
        n = len(c)
        dp = [0] * (v+1)
        for i in range(1, n+1):
            for j in range(c[i-1], v+1):
                dp[j] = max(dp[j], dp[j - c[i-1]] + w[i-1])
            print dp
        return dp[v]

    def coin_change(self, coins, amount):
        # 现有面额分别为coins的硬币，求凑出amount最少要几个硬币
        n = len(coins)
        dp = [float('+inf')] * (amount + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = min(dp[j], dp[j - coins[i-1]] + 1)
        return dp[amount] if dp[amount] != float('+inf') else -1

    def change(self, coins, amount):
        # 现有面额分别为coins的硬币，求凑出amount有多少种方式
        n = len(coins)
        dp = [0] * (amount + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            for j in range(coins[i - 1], amount + 1):
                dp[j] = dp[j] + dp[j - coins[i-1]]
        return dp[amount]

        
if __name__ == "__main__":
    Kp = Knapsack()

    # 0-1 naive problem
    if False:
        res = Kp.zero_one_pack_v2(v=11, c=[1,2,5,6,7], w=[1,6,18,22,28])
        print res

    if False:
        res = Kp.zero_one_pack_v3(v=11, c=[1,2,5,6,7], w=[1,6,18,22,28])
        print res

    if False:
        res = Kp.complete_pack(v=11, c=[1,2,5,6,7], w=[1,6,18,22,28])
        print res

    if False:
        res = Kp.coin_change(coins = [1, 2, 5], amount = 11)
        print res

    if True:
        res = Kp.change(coins = [1, 2, 5], amount = 5)
        print res

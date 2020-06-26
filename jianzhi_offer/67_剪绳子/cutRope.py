# -*- coding:utf-8 -*-
class Solution:
    def cutRope(self, number):
        # write code here
        if number < 3:
            return 1
        if number < 4:
            return 2
        if number < 5:
            return 4
        dp = [-1,-1,2,3,4]
        for i in range(5, number + 1):
            tmp = dp[i - 1]
            for j in range(i-2, 1, -1):
                cur = dp[j] * (i - j)
                if tmp < cur:
                    tmp = cur
            dp.append(tmp)
        return dp[-1]

if __name__ == '__main__':
    so = Solution()
    res = so.cutRope(8)
    print res

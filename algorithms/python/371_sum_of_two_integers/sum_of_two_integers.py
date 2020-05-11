# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/sum-of-two-integers

Calculate the sum of two integers a and b, but you are not allowed to use the operator + and -.

Example 1:
    Input: a = 1, b = 2
    Output: 3
Example 2:
    Input: a = -2, b = 3
    Output: 1
"""

class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        :idea: using bit logic operator
            for example:
                0 1 0 1    5
            +   0 1 0 0    4
            =   1 0 0 1    9
        as:
                0 1 0 1 ^ 0 1 0 0 = 0 0 0 1   ----- 0 0 0 1
                0 1 0 1 & 0 1 0 0 = 0 1 0 0 << 1 -- 1 0 0 0 +
                                                    1 0 0 1 =
        """
        MASK = 0x100000000  # 2 ^ 32
        # 有符号整型最大值
        MAX_INT = 0x7FFFFFFF
        MIN_INT = MAX_INT + 1
        while b != 0:
            carry = (a & b) << 1
            a = (a ^ b) % MASK
            b = carry % MASK
        return a if a <= MAX_INT else ~((a % MIN_INT) ^ MAX_INT)

if __name__ == "__main__":
    so = Solution()
    res = so.getSum(a=-12, b=-8)
    print res

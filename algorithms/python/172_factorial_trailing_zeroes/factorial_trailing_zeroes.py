# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/factorial-trailing-zeroes

Given an integer n, return the number of trailing zeroes in n!.

Example 1:
    Input: 3
    Output: 0
    Explanation: 3! = 6, no trailing zero.
Example 2:
    Input: 5
    Output: 1
    Explanation: 5! = 120, one trailing zero.

Note: Your solution should be in logarithmic time complexity.
"""
class Solution(object):

    def trailingZeroes(self, n):
        '''
            the method v2 still timeout
            for more:
                5: 5, 10, 15, 20...
                5*5: 25, 50, 75, 100...
                5*5*5: 125, 250, 375, 500...
            ...
            so that:
            res = n / 5 + n / 25 + n / 125 ...
            complexity: time O(log5 n)
        '''
        res = 0
        while n:
            n = n / 5
            res += n
        return res

    def trailingZeroes_v2(self, n):
        # iterative to see how many 2*5 pair
        # for more: the count of 2 >> 5, so we need only the number of 5
        res = 0
        while n:
            k = n
            while not k % 5:
                res += 1
                k = k / 5
            n -= 1
        return res

    def trailingZeroes_v1(self, n):
        """
        :type n: int
        :rtype: int
        :OT version
        """
        factorial = n
        for i in range(1, n):
            factorial *= i
        res = 0
        while factorial:
            if not factorial % 10:
                res += 1
            else:
                break
            factorial /= 10
        return res

if __name__ == '__main__':
    so = Solution()
    n = 30
    res = so.trailingZeroes(n)
    print res

# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/count-primes
Count the number of prime numbers less than a non-negative number, n.
Example:
    Input: 10
    Output: 4
    Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        :simulate the composite number
        :complexity: time O(nlglgn), space: O(n)
        """
        flags = [1] * (n)  # init : true - prime, false - composite
        for i in range(2, n):
            if flags[i]:
                t = 2
                while i * t < n:
                    flags[i * t] = 0
                    t += 1
        return sum(flags[2:])

if __name__ == "__main__":
    so = Solution()
    res = so.countPrimes(10)
    print res

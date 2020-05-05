# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/happy-number

Write an algorithm to determine if a number n is "happy".
A happy number is a number defined by the following process: 
    Starting with any positive integer, 
    replace the number by the sum of the squares of its digits, 
    and repeat the process until the number equals 1 (where it will stay), 
    or it loops endlessly in a cycle which does not include 1. 
    Those numbers for which this process ends in 1 are happy numbers.

Return True if n is a happy number, and False if not.

Example: 
    Input: 19
    Output: true
    Explanation: 
        12 + 92 = 82
        82 + 22 = 68
        62 + 82 = 100
        12 + 02 + 02 = 1
"""
class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        :simulate the process, using a hashset to record the val for repeatation check
        :complexity: time: O(log n), space: O(log n)
        """
        def getNext(x):
            res = 0
            while x:
                res += (x % 10) ** 2
                x = x / 10
            return res
        
        S = set()
        has_cycle = False
        while not has_cycle:
            if n == 1:
                return True
            if n in S:
                has_cycle = True
            S.add(n)
            n = getNext(n)
        return False

if __name__ == '__main__':
    S = Solution()
    n = 3
    res = S.isHappy(n)
    print res

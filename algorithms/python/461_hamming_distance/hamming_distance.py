# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/hamming-distance

The Hamming distance between two integers is the number of positions at which the corresponding bits are different.
Given two integers x and y, calculate the Hamming distance.

Note: 0 ≤ x, y < 231.

Example:
    Input: x = 1, y = 4
    Output: 2
    Explanation:
        1   (0 0 0 1)
        4   (0 1 0 0)
            ↑   ↑
The above arrows point to positions where the corresponding bits are different.
"""
class Solution(object):

    def hammingDistance(self, x, y):
        """
        :idea: based on v1, we can decrease the loop's cost
        :complexity: time: O(1), space: O(1)
        """
        res = 0
        z = x ^ y
        while z:
            res += 1
            z = z & (z - 1)
        return res

    def hammingDistance_v1(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        :idea: using XOR
        :complexity: time: O(1), space: O(1)
        """
        res = 0
        z = x ^ y
        while z:
            res += z % 2
            z = z >> 1
        return res

if __name__ == "__main__":
    so = Solution()
    x = 1
    y = 4
    res = so.hammingDistance(x, y)
    print res

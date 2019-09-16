# coding: utf8
# python 2.7
"""
Given a string s, find the longest palindromic substring in s. 
You may assume that the maximum length of s is 1000.

- Example 1:
    Input: "babad"
    Output: "bab"
    Note: "aba" is also a valid answer.
- Example 2:
    Input: "cbbd"
    Output: "bb"
"""

class Solution(object):

    def longestPalindrome_2(self, s):
        """
        :改进1: 
            回文特点,关于中心轴对称,该轴即可以是1个数字,也可以是两个连续重复数字
            于是遍历,分别考虑上述两种情况        
        """

    def longestPalindrome_1(self, s):
        """
        :type s: str
        :rtype: str
        :方法1: 
            回文特点,关于中心轴对称,该轴即可以是1个数字,也可以是两个连续重复数字
            于是遍历,分别考虑上述两种情况
            O(n^2)
        """
        n = len(s)
        res = ''
        for i in range(n):
            # 以i为轴
            tmp = '' + s[i]
            j = i - 1
            k = i + 1
            while j >= 0 and k < n:
                if s[j] != s[k]:
                    break
                else:
                    tmp = s[j] + tmp + s[k]
                j -= 1
                k += 1
            if len(tmp) > len(res):
                res = tmp
            # 以i和i+1为轴
            if i + 1 < n and s[i] == s[i + 1]:
                tmp = '' + s[i:i+2]
                j = i - 1
                k = i + 2
                while j >= 0 and k < n:
                    if s[j] != s[k]:
                        break
                    else:
                        tmp = s[j] + tmp + s[k]
                    j -= 1
                    k += 1
                if len(tmp) > len(res):
                    res = tmp
        return res


if __name__ == "__main__":
    st = 'abcdedcba'
    s = Solution()
    res = s.longestPalindrome_2(st)
    print res

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
        :采用 force-brute + DP, dp[i][j]->s[i,j]是否是回文
        """
        n = len(s)
        dp = [[False for i in range(n)] for j in range(n)]
        res = ''
        for m in range(n):  # 潜在字符串长度
            for i in range(n-m):
                if m == 0:
                    dp[i][i] = True
                elif m == 1:
                    dp[i][i+m] = (s[i] == s[i+m])
                else:
                    dp[i][i+m] = dp[i+1][i+m-1] and s[i] == s[i+m]
                if dp[i][i+m]:
                    res = s[i:i+m+1]
        return res

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
    st = 'babad'
    s = Solution()
    res = s.longestPalindrome_2(st)
    print res

# coding: utf8
# python 2.7
"""
@Link: https://leetcode-cn.com/problems/valid-palindrome-ii

@Problem: Given a non-empty string s, you may delete at most one character. 
          Judge whether you can make it a palindrome.

@Examples:
    1:
        Input: "aba"
        Output: True

    2:
        Input: "abca"
        Output: True
        Explanation: You could delete the character 'c'.
"""

class Solution(object):

    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        :idea: compare from two side, when dismatch appear, try to remove one of then to see if string left is valid.
        :complexity: time O(n), space O(1)
        :implement: using iteration & recursion
        """
        def func(s, k):
            i, j = 0, len(s) - 1
            while i < j:
                if s[i] != s[j]:
                    return k > 0 and (func(s[i+1:j+1], k-1) or func(s[i:j], k-1))
                else:
                    i += 1
                    j -= 1
            return True

        return func(s, 1)

    def validPalindrome_v1(self, s):
        """
        :type s: str
        :rtype: bool
        :idea: compare from two side, when dismatch appear, try to remove one of then to see if string left is valid.
        :complexity: time O(n), space O(1)
        :implement: using recursion, may be too deep
        """
        def func(s, k):
            # k is the chance to remove one, in this problem k<=1
            if not s:
                return True
            if s[0] == s[-1]:
                return func(s[1: -1], k)
            elif k > 0:
                return func(s[1:], k - 1) or func(s[:-1], k - 1)
            else:
                return False

        return func(s, 1)

if __name__ == "__main__":
    so = Solution()
    st = "abcda"
    res = so.validPalindrome(st)
    print res

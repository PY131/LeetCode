# coding: utf8
# python 2.7
"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:
    Input: "A man, a plan, a canal: Panama"
    Output: true

Example 2:
    Input: "race a car"
    Output: false
"""

class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        :idea: using stack(FILO) & queue(FIFO) and compare one by one
        :complexity: time O(n), space O(n)
        """
        S = []
        for x in s.lower():
            if x.isalnum():
                S.append(x)
        for i in range(len(S)/2):
            if S[i] != S[-(i+1)]:
                return False
        return True

if __name__ == "__main__":
    so = Solution()
    st = "A man, a plan, a canal: Panama"
    st = ""
    res = so.isPalindrome(st)
    print res

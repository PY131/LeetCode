# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/reverse-string

Write a function that reverses a string. The input string is given as an array of characters char[].
Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.
You may assume all the characters consist of printable ascii characters.

Example 1:
    Input: ["h","e","l","l","o"]
    Output: ["o","l","l","e","h"]
Example 2:
    Input: ["H","a","n","n","a","h"]
    Output: ["h","a","n","n","a","H"]
"""

class Solution(object):
    def reverseString(self, s):
        """
        :type s: List[str]
        :rtype: None Do not return anything, modify s in-place instead.
        """
        N = len(s)
        for i in range(N / 2):
            s[i], s[N - 1 - i] = s[N - 1 - i], s[i]
        # complexity: time - O(N), space - O(1)

if __name__ == "__main__":
    so = Solution()
    st = ["h","e","l","l","o"]
    so.reverseString(st)
    print st


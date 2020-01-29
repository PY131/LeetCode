# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Return the index of the first occurrence of needle in haystack, 
    or -1 if needle is not part of haystack.

@example:
    Input: haystack = "hello", needle = "ll"
    Output: 2
    ps. if "" return 0
"""

class Solution(object):

    def strStr_3(self, haystack, needle):
        """using KMP"""

        def build_next(needle):
            m = len(needle)
            res = [-1] * m
            i = 0
            j = -1
            while i < m - 1:
                if j < 0 or needle[i] == needle[j]:
                    i += 1
                    j += 1
                    res[i] = j if needle[i] != needle[j] else res[j]
                else:
                    j = res[j]
            return res

        n = len(haystack)
        m = len(needle)
        next = build_next(needle)
        i = 0
        j = 0
        while i < n and j < m:
            if j < 0 or haystack[i] == needle[j]:
                i += 1
                j += 1
            else:
                j = next[j]
        return i - j if j == m else -1

    def strStr_2(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        :method: the same as method 1
        e.g:
            haystack = "...ooo..."
                           |
                           i
            needle = "xxx"
                      |
                      j
            if i == j then compare i+1 & j+1
            else: i++ and compare i & j
        """
        n = len(haystack)
        m = len(needle)
        i = 0
        while i <= n - m:
            j = 0
            while j < m and i + j < n:
                if haystack[i+j] != needle[j]:
                    break
                j += 1
            if j == m and i + j <= n:
                return i
            i += 1
        return -1

    def strStr_1(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        :method: e.g:
            haystack = "...ooo..."
            needle = "xxx" length of 3
            if result is i -> "...ooo..."
                                  |
                                  i
                                  haystack[i: i+3] = "ooo" = needle = "xxx"
        """
        n = len(haystack)
        m = len(needle)
        i = 0
        while i <= n-m:
            if haystack[i: i+m] == needle:            
                return i
            i += 1
        return -1

if __name__ == '__main__':
    s = Solution()
    haystack = "abababdabababca"
    needle = "abababca"
    haystack = "aaaaa"
    needle = "bba"
    res = s.strStr_3(haystack, needle)
    print res
    
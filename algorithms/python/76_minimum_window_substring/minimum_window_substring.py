# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/minimum-window-substring/

Given a string S and a string T, find the minimum window in S which will contain all the characters in T in complexity O(n).

Example:
    Input: S = "ADOBECODEBANC", T = "ABC"
    Output: "BANC"

Note:
    If there is no such window in S that covers all characters in T, return the empty string "".
    If there is such window, you are guaranteed that there will always be only one unique minimum window in S.
"""
class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        n = len(s)
        m = len(t)
        if n == 0 or m == 0 or n < m:
            return ""

        map_w = {}
        map_t = {}
        for x in t:
            map_t[x] = map_t.get(x, 0) + 1
        dis = 0

        min_len = n + 1
        min_idx = 0
        res = ""
        l = r = 0
        while r < n:
            # shift right
            if s[r] not in map_t:
                r += 1
                continue
            
            map_w[s[r]] = map_w.get(s[r], 0) + 1
            if map_w[s[r]] <= map_t[s[r]]:
                dis += 1
            r += 1

            while dis == m:
                while s[l] not in map_t:  # shift left
                    l += 1
                
                if r - l < min_len:
                    min_len = r - l
                    min_idx = l
                
                if map_w[s[l]] == map_t[s[l]]:
                    dis -= 1
                map_w[s[l]] -= 1
                l += 1
            
        return "" if min_len > n else s[min_idx: min_idx + min_len]

if __name__ == '__main__':
    so = Solution()
    S = "ADOBECODEBANC"
    T = "ABC"
    res = so.minWindow(S, T)
    print res

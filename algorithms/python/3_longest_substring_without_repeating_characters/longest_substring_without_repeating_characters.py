# coding: utf8
# python 2.7
"""
- Problem:
    Given a string, find the length of the longest substring without repeating characters.

- Example 1:
    Input: "abcabcbb"
    Output: 3 
    Explanation: The answer is "abc", with the length of 3. 
- Example 2:
    Input: "bbbbb"
    Output: 1
    Explanation: The answer is "b", with the length of 1.
- Example 3:
    Input: "pwwkew"
    Output: 3
    Explanation: The answer is "wke", with the length of 3. 
        Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

class Solution(object):

    def lengthOfLongestSubstring_1(self, s):
        """
        :type s: str
        :rtype: int
        :method: 直接向后遍历, 对每个起始, 采用map记录当前遍历过的char -> O(n^2)
        """
        n = len(s)
        len_max = 0
        for i in range(n):
            D = {}
            j = i
            while j < n:
                if s[j] not in D:
                    D[s[j]] = 1
                else:
                    break
                j += 1
            len_tmp = j - i
            if len_tmp > len_max:
                len_max = len_tmp
        return len_max

    def lengthOfLongestSubstring_2(self, s):
        # 改进前面的map,每次循环共享map,map记录下标（重复元素记录最新）
        n = len(s)
        len_max = 0
        D = {}
        i, j = 0, 0
        while i < n and j < n:
            if s[j] in D:
                if j - i > len_max:
                    len_max = j - i
                new_i = D[s[j]] + 1
                while i < new_i:  # i -> new_i
                    D.pop(s[i])
                    i += 1
            D[s[j]] = j  # record newest s[j] index
            j += 1  # j -> new_j
        if j == n:
            len_tmp = j - i
            if len_tmp > len_max:
                len_max = len_tmp     
        return len_max

    def lengthOfLongestSubstring_3(self, s):
        # 解法2本质是构造了一个滑动窗口, 更简介写如下
        # 滑窗范围为[i, j)
        n = len(s)
        len_max = 0
        slide = []
        i, j = 0, 0
        while i < n and j < n:
            if s[j] in slide:
                if j - i > len_max:
                    len_max = j - i
                while i < j:
                    i += 1
                    if slide.pop(0) == s[j]:
                        break
            slide.append(s[j])
            j += 1
        if j == n:
            len_tmp = j - i
            if len_tmp > len_max:
                len_max = len_tmp        
        return len_max


if __name__ == "__main__":
    st = 'abcabcbb'
    s = Solution()
    res = s.lengthOfLongestSubstring_1(st)
    print res
    res = s.lengthOfLongestSubstring_2(st)
    print res
    res = s.lengthOfLongestSubstring_3(st)
    print res
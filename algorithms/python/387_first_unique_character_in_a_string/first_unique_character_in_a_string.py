# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/first-unique-character-in-a-string

Given a string, find the first non-repeating character in it and return it's index. 
If it doesn't exist, return -1.

Examples:

    s = "leetcode"
    return 0.

    s = "loveleetcode",
    return 2.

Note: You may assume the string contain only lowercase letters.
"""

class Solution(object):

    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        :idea: 
            - using one map to record the count of each appears and first index
        :complexity: time: O(n), space: O(n)
        """
        M = {}
        for idx, ch in enumerate(s):
            if ch not in M:
                M[ch] = {'cnt': 1, '1st_idx': idx}
            else:
                M[ch]['cnt'] += 1

        idx_min = len(s)
        for ch in M:
            if M[ch]['cnt'] == 1 and M[ch]['1st_idx'] < idx_min:
                idx_min = M[ch]['1st_idx']
        
        return idx_min if idx_min < len(s) else -1

if __name__ == "__main__":
    so = Solution()
    st = "leetcode"
    # st = "loveleetcode"
    res = so.firstUniqChar(st)
    print res


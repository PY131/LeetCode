# coding: utf8
# python 2.7
"""
Link: https://leetcode.com/problems/group-anagrams
Given an array of strings, group anagrams together.
Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
    Output:
    [
        ["ate","eat","tea"],
        ["nat","tan"],
        ["bat"]
    ]
Note:
    All inputs will be in lowercase.
    The order of your output does not matter.
"""
from collections import defaultdict

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        M = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord('a')] += 1
            M["".join(map(str, count))].append(s)
        return M.values()

if __name__ == '__main__':
    S = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = S.groupAnagrams(strs)
    print res

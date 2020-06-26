# -*- coding:utf-8 -*-
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        x2cnt = {}
        for x in s:
            if x in x2cnt:
                x2cnt[x] += 1
            else:
                x2cnt[x] = 1
        for i in range(len(s)):
            if x2cnt.get(s[i], 0) == 1:
                return i
        return -1

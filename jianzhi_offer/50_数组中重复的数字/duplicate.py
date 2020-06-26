# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        S = set()
        for x in numbers:
            if x not in S:
                S.add(x)
            else:
                duplication[0] = x
                return True
        return False
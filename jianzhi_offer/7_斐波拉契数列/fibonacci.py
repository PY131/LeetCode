# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        if n < 2:
            return n
        pre = 0
        cur = 1
        for i in range(2, n + 1):
            cur = cur + pre
            pre = cur - pre
        return cur
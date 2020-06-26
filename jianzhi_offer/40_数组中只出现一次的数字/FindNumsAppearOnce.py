# -*- coding:utf-8 -*-
class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        xor = 0
        for x in array:
            xor = xor ^ x
        mask = 1
        while mask & xor == 0:
            mask = mask << 1
        xor_1 = 0
        xor_2 = 0
        for x in array:
            if mask & x == 0:
                xor_1 = xor_1 ^ x
            else:
                xor_2 = xor_2 ^ x
        return xor_1, xor_2
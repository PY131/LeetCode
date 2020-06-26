# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # write code here
        n = len(array)
        new_array = [0] * n
        k = p = 0
        while p < n:
            if array[p] % 2 == 1:
                new_array[k] = array[p]
                k += 1
            p += 1
        k = p = n - 1
        while p >= 0:
            if array[p] % 2 == 0:
                new_array[k] = array[p]
                k -= 1
            p -= 1
        return new_array
# -*- coding:utf-8 -*-
class Solution:
    def multiply(self, A):
        # write code here
        B = []
        C = []
        prod_1 = 1
        prod_2 = 1
        i = 0
        n = len(A)
        for i in range(n):
            B.append(prod_1)
            C.append(prod_2)
            prod_1 *= A[i]
            prod_2 *= A[n - 1 - i]
        for i in range(n):
            B[i] = B[i] * C[n - 1 - i]
        return B
# -*- coding:utf-8 -*-
class Solution:
    
    def findRange(self, data, lo, hi, k):
        while lo <= hi:
            mi = (lo + hi) >> 1
            if data[mi] < k:
                lo = mi + 1
            elif data[mi] > k:
                hi = mi - 1
            else:
                return self.findRange(data, lo, mi - 1, k) + self.findRange(data, mi + 1, hi, k) + 1
        return hi - lo + 1
        
    def GetNumberOfK(self, data, k):
        # write code here
        return self.findRange(data, 0, len(data) - 1, k)
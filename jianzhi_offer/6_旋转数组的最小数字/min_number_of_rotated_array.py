# -*- coding:utf-8 -*-
class Solution:
    def minNumberInRotateArray(self, rotateArray):        
        def help(arr, lo, hi):
            while lo < hi:
                if arr[lo] < arr[hi]:
                    break
                mi = (lo + hi) >> 1
                if arr[mi] > arr[lo]:
                    lo = mi + 1
                elif arr[mi] < arr[hi]:
                    hi = mi
                else:
                    lo += 1
            return arr[lo]
        
        if not rotateArray:
            return 0
        return help(rotateArray, 0, len(rotateArray) - 1)

if __name__ == "__main__":
    arr = [4,5,1,2,3]
    so = Solution()
    res = so.minNumberInRotateArray(arr)
    print res
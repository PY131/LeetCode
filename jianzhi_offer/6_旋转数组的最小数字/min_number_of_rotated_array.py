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

    def minArray(self, numbers):
        """
        :type numbers: List[int]
        :rtype: int
        """
        lo = 0
        hi = len(numbers) - 1
        while lo < hi:
            mi = (lo + hi) / 2
            if numbers[mi] < numbers[hi]:
                hi = mi
            elif numbers[mi] > numbers[hi]:
                lo = mi + 1
            else:
                hi -= 1
        return numbers[lo]

if __name__ == "__main__":
    arr = [1,2,3]
    so = Solution()
    res = so.minArray(arr)
    print res
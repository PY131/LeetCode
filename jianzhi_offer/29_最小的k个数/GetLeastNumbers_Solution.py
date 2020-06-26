# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here# write code here
        def build_a_max_heap(nums, n):
            # cost O(K)
            for i in range((n-1)/2, -1, -1):
                adjust(nums, i, n)
            
        def adjust(nums, i, n):
            # cost O(logK)
            while 2 * i + 1 < n:
                k = 2 * i + 1
                r = 2 * i + 2
                if r < n and nums[r] > nums[k]:
                    k = r
                nums[i], nums[k] = nums[k], nums[i]
                i = k
            
        n = len(tinput)
        if k > n or k == 0:
            return []
        res = tinput[0:k]
        build_a_max_heap(res, k)

        for i in range(k, n):
            if tinput[i] < res[0]:
                res[0] = tinput[i]
                adjust(res, 0, k)
        res.sort()
        return res

if __name__ == '__main__':
    arr = [4,5,1,6,2,7,3,8]
    so = Solution()
    res = so.GetLeastNumbers_Solution(arr, 4)
    print res
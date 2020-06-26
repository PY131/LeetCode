# -*- coding:utf-8 -*-

class Solution:
    def InversePairs(self, data):
        # write code here
        # O(n^2)
        n = len(data)
        res = 0
        for i in range(n):
            for j in range(i + 1, n):
                if data[i] > data[j]:
                    res += 1
        return res % 1000000007

    def InversePairs_v1(self, data):
        # using bi-search to decrease complexity to O(nlogn)
        # write code here
        def find_index(nums, target):
            lo = 0
            hi = len(nums) - 1
            while lo <= hi:
                mi = (lo + hi) >> 1
                if nums[mi] <= target:
                    hi = mi - 1
                else:
                    lo = mi + 1
            return lo
        
        res = 0
        tmp = []
        for x in data:
            idx = find_index(tmp, x)
            res += idx
            tmp.insert(idx, x)
        return res


    def InversePairs_v2(self, data):
        # write code here
        n = len(data)
        self.tmp = [0] * n
        self.res = 0
        
        def merge_sort(nums, lo, hi):
            if lo >= hi:
                return
            mi = (lo + hi) >> 1
            merge_sort(nums, lo, mi)
            merge_sort(nums, mi + 1, hi)
            merge_two(nums, lo, mi, hi)
            
        def merge_two(nums, lo, mi, hi):
            k = lo
            i = lo
            j = mi + 1
            while k <= hi:
                if i <= mi and j <= hi:
                    if nums[i] <= nums[j]:
                        self.tmp[k] = nums[i]
                        i += 1
                    else:
                        self.tmp[k] = nums[j]
                        j += 1
                        self.res += mi - i + 1
                elif i <= mi:
                    self.tmp[k] = nums[i]
                    i += 1
                else:
                    self.tmp[k] = nums[j]
                    j += 1
                k += 1
            k = lo
            while k <= hi:
                nums[k] = self.tmp[k]
                k += 1

        merge_sort(data, 0, n - 1)
        return self.res

if __name__ == '__main__':
    arr = [7,5,6,4,8]
    so = Solution()
    res = so.InversePairs_v2(arr)
    print res
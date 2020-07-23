# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/sort-an-array

Given an array of integers nums, sort the array in ascending order.
Example 1:
    Input: nums = [5,2,3,1]
    Output: [1,2,3,5]
Example 2:
    Input: nums = [5,1,1,2,0,0]
    Output: [0,0,1,1,2,5]
"""

class Solution(object):
    
    def bubble_sort(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            done = True
            for j in range(1, n-i):
                if nums[j-1] > nums[j]:
                    nums[j-1], nums[j] = nums[j], nums[j-1]
                    done = False
            if done:
                break
            i += 1
        return nums

    def select_sort(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
            i += 1
        return nums

    def merge_sort(self, nums, lo, hi):
        def merge(nums, lo, mi, hi):
            # assert is_sorted(nums[lo: mi+1]) is true
            # assert is_sorted(nums[mi+1: hi+1]) is true
            tmp = []
            i = lo
            j = mi + 1
            while i <= mi and j <= hi:
                while i <= mi and nums[i] <= nums[j]:
                    tmp.append(nums[i])
                    i += 1
                while j <= hi and nums[i] > nums[j]:
                    tmp.append(nums[j])
                    j += 1
            while i <= mi:
                tmp.append(nums[i])
                i += 1
            while j <= hi:
                tmp.append(nums[j])
                j += 1
            nums[lo: hi+1] = tmp

        if hi - lo < 1:
            return nums
        mi = (lo + hi) >> 1
        self.merge_sort(nums, lo, mi)
        self.merge_sort(nums, mi+1, hi)
        merge(nums, lo, mi, hi)
        return nums

    def heap_sort(self, nums, lo, hi):
        
        def adjust(nums, p, hi):
            while p <= hi:
                l = 2 * p + 1
                r = 2 * p + 2
                k = l
                if r <= hi and nums[r] > nums[l]:
                    k = r
                if k <= hi and nums[k] > nums[p]:
                    nums[k], nums[p] = nums[p], nums[k]
                    p = k
                else:
                    break
        
        def build_heap(nums, lo, hi):
            p = hi / 2 - 1
            while p >= lo:
                adjust(nums, p, hi)
                p -= 1
        
        build_heap(nums, lo, hi)
        i = hi
        while i > lo:
            nums[i], nums[lo] = nums[lo], nums[i]
            adjust(nums, lo, i - 1)
            i -= 1
        return nums

    def quick_sort(self, nums, lo, hi):
        if not lo < hi:
            return nums
        i = lo
        j = hi
        p = i
        tmp = nums[p]
        while i < j:
            while i < j and nums[j] >= tmp:
                j -= 1
            nums[p] = nums[j]
            p = j
            while i < j and nums[i] <= tmp:
                i += 1
            nums[p] = nums[i]
            p = i
        nums[p] = tmp
        self.quick_sort(nums, lo, p-1)
        self.quick_sort(nums, p+1, hi)
        return nums
    
    def sortArray(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = self.quick_sort(nums, 0, len(nums) - 1)
        return res

if __name__ == "__main__":
    so = Solution()
    nums = [5,1,1,2,0,0]
    res = so.sortArray(nums)
    print res
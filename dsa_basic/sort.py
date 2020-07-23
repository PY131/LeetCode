# -*- coding: utf-8 -*-

import random, copy, time

class Sorter(object):

    def bubble_sort(self, nums):
        n = len(nums)
        for i in range(n):
            for j in range(1, n - i):
                if nums[j] < nums[j - 1]:
                    nums[j - 1], nums[j] = nums[j], nums[j - 1]
        return

    def selection_sort(self, nums):
        n = len(nums)
        for i in range(n):
            min_idx = i
            for j in range(i+1, n):
                if nums[j] < nums[min_idx]:
                    min_idx = j
            nums[min_idx], nums[i] = nums[i], nums[min_idx]
        return

    def heap_sort(self, nums):
        n = len(nums)
        
        def adjust(p, hi):
            while p <= hi:
                l = 2*p + 1
                r = 2*p + 2
                k = l
                if r <= hi and nums[r] > nums[k]:
                    k = r
                if k <= hi and nums[k] > nums[p]:
                    nums[p], nums[k] = nums[k], nums[p]
                else:
                    break

        def build():
            for i in range(n/2 - 1, -1, -1):
                adjust(i, n-1)

        build()
        for i in range(n-1, 0, -1):
            nums[0], nums[i] = nums[i], nums[0]
            adjust(0, i-1)
        return

    def merge_sort(self, nums):
        n = len(nums)
        tmp = [0] * n

        def merge_two(lo, mi, hi):
            i = lo
            j = mi + 1
            p = lo
            while i <= mi and j <= hi:
                while i <= mi and nums[i] <= nums[j]:
                    tmp[p] = nums[i]
                    i += 1
                    p += 1
                while j <= hi and nums[i] > nums[j]:
                    tmp[p] = nums[j]
                    j += 1
                    p += 1
            while i <= mi:
                tmp[p] = nums[i]
                i += 1
                p += 1
            while j <= hi:
                tmp[p] = nums[j]
                j += 1
                p += 1
            
            nums[lo: hi+1] = tmp[lo: hi+1]

        def partition(lo, hi):
            if hi - lo < 1:
                return
            mi = (lo + hi) >> 1
            partition(lo, mi)
            partition(mi+1, hi)
            merge_two(lo, mi, hi)
            return

        partition(0, n-1)
        return

    def quick_sort(self, nums):
        n = len(nums)
        
        def partition(lo, hi):
            i = lo
            j = hi
            tmp = nums[lo]
            while i < j:
                while i < j and tmp <= nums[j]:
                    j -= 1
                nums[i] = nums[j]
                while i < j and tmp > nums[i]:
                    i += 1
                nums[j] = nums[i]
            nums[i] = tmp
            return i

        def help(lo, hi):
            if hi - lo < 1:
                return
            mi = partition(lo, hi)
            help(lo, mi)
            help(mi+1, hi)

        help(0, n-1)
        return

    def color_sort(self, nums):
        i = 0
        j = len(nums) - 1
        p = 0
        while p <= j:
            while p <= j and nums[p] == 2:
                nums[p], nums[j] = nums[j], nums[p]
                j -= 1
            while p <= j and nums[p] == 0:
                nums[p], nums[i] = nums[i], nums[p]
                i += 1
                p += 1
            p += 1

if __name__ == "__main__":
    sorter = Sorter()

    # generate random array list
    raw_list = []
    for _ in range(3000):
        raw_list.append(random.randint(0, 1000000))

    # built-in sort
    nums = copy.copy(raw_list)
    st = time.time()
    nums.sort()
    ed = time.time()
    print "using built-in sort, time cost: %.3f ms" % (1000 * (ed - st))

    # sort
    for func_name in ['bubble_sort', 'selection_sort', 'heap_sort', 'merge_sort', 'quick_sort']:
        nums = copy.copy(raw_list)
        st = time.time()
        func = getattr(sorter, func_name)
        func(nums)
        ed = time.time()
        print "using %s, time cost: %.3f ms" % (func_name, 1000 * (ed - st))

    # three color sort
    nums = [1,2,0,1,1,2,0,0,2]
    sorter.color_sort(nums)
    print nums[0:10]


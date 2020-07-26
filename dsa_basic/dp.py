# -*- coding: utf-8 -*-

class DynamicProgrammer():

    def fibonacci(self, n):
        # 斐波那契数列第n项
        if n < 1:
            return 0
        f0 = 0
        f1 = 1
        for _ in range(2, n+1):
            f1 = f1 + f0
            f0 = f1 - f0
        return f1

    def max_sum_of_subarray(self, nums):
        # 连续子数组的最大和
        n = len(nums)
        res = nums[0]
        s = nums[0]
        for i in range(1, n):
            s = s + nums[i] if s > 0 else nums[i]
            if res < s:
                res = s
        return res

    def length_of_LIS(self, nums):
        # 最长的上升子序列
        arr = []
        for x in nums:
            print "before:", arr, x
            if not arr or arr[-1] < x:
                arr.append(x)
                continue
            lo = 0
            hi = len(arr) - 1
            loc = hi
            while lo <= hi:
                mi = (lo + hi) / 2
                if nums[mi] >= x:
                    loc = mi
                    hi = mi - 1
                else:
                    lo = mi + 1
            arr[loc] = x
            print "after:", arr, lo
        return len(arr)

if __name__ == "__main__":
    DP = DynamicProgrammer()

    # fibonacci
    if False:
        N = 10
        print "the %sth nnumber of fibonacci array is:%s" % (N, DP.fibonacci(N))

    # max sum of continuous sub array
    if False:
        nums = [-2,1,-3,4,-1,2,1,-5,4]
        print DP.max_sum_of_subarray(nums)

    # length of longest increasing sub array
    if False:
        nums = [10,9,2,5,3,7,101,18]
        print DP.length_of_LIS(nums)

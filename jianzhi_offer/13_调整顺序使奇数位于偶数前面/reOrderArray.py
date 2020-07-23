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
    
    def exchange(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        j = len(nums) - 1
        p = 0
        while p <= j:



            
            print nums
            print i, j, p, nums[i], nums[j], nums[p]
            if nums[p] % 2 != 0:  # odd
                nums[i], nums[p] = nums[p], nums[i]
                i += 1
                p += 1
            else:  # even
                nums[j], nums[p] = nums[p], nums[j]
                j -= 1
        return nums

if __name__ == "__main__":
    arr = [2,16,3,5,13,1,16,1,12,18,11,8,11,11,5,1]
    so = Solution()
    res = so.exchange(arr)
    print res
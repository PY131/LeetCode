# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Implement next permutation, 
    which rearranges numbers into the lexicographically next greater permutation of numbers.

    If such arrangement is not possible, 
    it must rearrange it as the lowest possible order (ie, sorted in ascending order).
    The replacement must be in-place and use only constant extra memory.

Here are some examples. 
    Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
    1,2,3 → 1,3,2
    3,2,1 → 1,2,3
    1,1,5 → 1,5,1
"""

class Solution(object):

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        i = n - 1  # search from end to start
        # find the first revert item
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        i -= 1
        # print i, nums[i], nums
        # find the smallest item larger than nums[i]
        if i >= 0:
            j = i + 1
            while j < n and nums[i] < nums[j]:
                j += 1
            j -= 1
            # print j, nums[j], nums
            # swap
            if i != j:
                tmp = nums[j]
                nums[j] = nums[i]
                nums[i] = tmp
        # sort between i+1 -> n
        i += 1
        j = n - 1
        while i < j:
            tmp = nums[j]
            nums[j] = nums[i]
            nums[i] = tmp
            i += 1
            j -= 1

if __name__ == '__main__':
    s = Solution()
    nums = [1,5,1,5,1]
    s.nextPermutation(nums)
    print nums
    

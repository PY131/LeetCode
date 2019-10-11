# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Given a sorted array nums, 
    remove the duplicates in-place such that each element appear only once, and return the new length.

    Do not allocate extra space for another array, 
    you must do this by modifying the input array in-place with O(1) extra memory.

@example:
    Given nums = [1,1,2],
    Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.
    It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):

    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :method 1: use two indexs
            step-1: 1   1   2   3
                    |   |
                    v   v
                    i   j -> same

            step-2: 1   1   2   3
                    |       |
                    v       v
                    i       j -> different

            step-3: 1   2   2   3   (put j to i + 1)
                        |       |
                        v       v
                        i       j -> different
                        
            step-4: 1   2   3   3   (put j to i + 1)
                            |       |
                            v       v
                            i       j -> end
        """
        if len(nums) < 2: return len(nums)
        i = 0
        j = 1
        while j < len(nums):
            # different
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0,0,1,1,1,2,2,3,3,4]
    res = s.removeDuplicates(nums)
    print res, nums[0: res]
    

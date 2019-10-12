# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Given an array nums and a value val, 
    remove all instances of that value in-place and return the new length.

    Do not allocate extra space for another array, 
    you must do this by modifying the input array in-place with O(1) extra memory.
    The order of elements can be changed. 
    It doesn't matter what you leave beyond the new length

@example:
    Given nums = [3,2,2,3], val = 3,
    Your function should return length = 2, with the first two elements of nums being 2.

"""

class Solution(object):

    def removeElement_2(self, nums, val):
        """
        like method 1, 
        when the elements to be deleted are only a small part of all,
        the swap between i, j is cost-effective.
        we can also swap the item of target with the last one (in fact we can only align the current=last one)
        for example:
            s1:  [3, 2, 2, 3]  val = 2
                  |        |
                  v        v
                  j        i

            s2:  [3, 2, 2, 3]
                     |     |
                     v     v
                     j     i  -> j hit swap(nums i, j)

            s3:  [3, 3, 2, 2]
                     |  |
                     v  v
                     j  i

            s4:  [3, 3, 2, 2]
                        ||
                        vv
                        ji  -> hit swap(nums i, j)

            s5:  [3, 3, 2, 2]
                     |  |
                     v  v
                     i  j  j > i return i + 1
        """
        i = len(nums) - 1
        j = 0
        while j <= i:
            if nums[j] == val:
                nums[j] = nums[i]
                i -= 1
            else:
                j += 1
        return i + 1

    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        :method: similar as 26, using two pointer
        """
        i = -1
        j = 0
        while j < len(nums):
            if nums[j] != val:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1

if __name__ == '__main__':
    s = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    res = s.removeElement_2(nums, val)
    print res, nums[0: res]
    

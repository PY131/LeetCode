# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/single-number

Given a non-empty array of integers, 
every element appears twice except for one. Find that single one.

Note:
    Your algorithm should have a linear runtime complexity. 
    Could you implement it without using extra memory?

Example 1:
    Input: [2,2,1]
    Output: 1

Example 2:
    Input: [4,1,2,1,2]
    Output: 4
"""

class Solution(object):

    def singleNumber(self, nums):
        """
        :using XOR, as a XOR a = 0, a XOR b XOR a = b
        :complexity: time: O(n), space: O(1)
        """
        res = nums[0] if nums else None
        for x in nums[1:]:
            res ^= x
        return res

    def singleNumber_v3(self, nums):
        """
        :method: we can use hashmap to record each appear count, then find that appears only once
        :complexity: time: O(n), space: O(n)
        """
        M = {}
        for num in nums:
            if num in M:
                M[num] += 1
            else:
                M[num] = 1
        for num in nums:
            if M[num] == 1:
                return num 
        return None

    def singleNumber_v2(self, nums):
        """
        :method: on the base of v1, using python build-in sort func
        """
        nums.sort()
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums[-1]

    def singleNumber_v1(self, nums):
        """
        :method: on the base of v0, we can do sort first, then iterative
        :complexity: time: O(nlogn), space: O(1)
        """
        # use heap (small) sort as example
        def heap_sort(nums, lo, hi):
            
            def adjust(nums, i, hi):
                # down filter two ensure sub-tree is parent>child
                while i < hi:
                    lc = 2 * i + 1
                    rc = 2 * i + 2
                    kc = lc
                    if rc <= hi and nums[lc] < nums[rc]:
                        kc = rc
                    if kc <= hi and nums[i] < nums[kc]:
                        nums[i], nums[kc] = nums[kc], nums[i]
                    i = kc

            # build heap O
            for i in range(hi / 2 - 1, lo - 1, -1):
                adjust(nums, i, hi)
            # get biggest
            for i in range(hi, lo-1, -1):
                nums[i], nums[0] = nums[0], nums[i]
                adjust(nums, 0, i-1)

        heap_sort(nums, 0, len(nums) - 1)
        i = 0
        while i < len(nums) - 1:
            if nums[i] != nums[i+1]:
                return nums[i]
            i += 2
        return nums[-1]

    def singleNumber_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        :method: force-brute, twice iteration
        :complexity: time - O(n^2), space - O(1)
        """
        N = len(nums)
        res = None
        for i in range(N):
            flag = False  # whether repeated
            for j in range(N):
                if i != j and nums[i] == nums[j]:
                    flag = True
                    break
            if not flag:
                res = nums[i]
                break
        return res

if __name__ == "__main__":
    so = Solution()
    arr = [2,2,1]
    res = so.singleNumber(arr)
    print res

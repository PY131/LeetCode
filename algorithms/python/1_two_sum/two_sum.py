# coding: utf8
# python 2.7
"""
- Problem:
    Given an array of integers, return indices of the two numbers such that they add up to a specific target.
    You may assume that each input would have exactly one solution, and you may not use the same element twice.

- Example:
    Given nums = [2, 7, 11, 15], target = 9,
    Because nums[0] + nums[1] = 2 + 7 = 9,
    return [0, 1].
"""

class Solution(object):

    # 直接暴力求解 -> O(n^2)
    def twoSum_1(self, nums, target):
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []

    # 直接暴力求解2 -> O(n^2)
    def twoSum_2(self, nums, target):
        n = len(nums)
        for i in range(n):
            tar = target - nums[i]
            for j in range(i+1, n):
                if nums[j] == tar:
                    return [i, j]
        return []

    # 空间换时间 --> O(n)
    # hash map: k = num, val = index
    def twoSum_3(self, nums, target):
        M = {}
        for idx, x in enumerate(nums):
            M[x] = idx
        for idx, x in enumerate(nums):
            sub = target - x
            if sub in M and idx != M[sub]:
                return [idx, M[sub]]  # assert idx < idx2
        return []

    # 空间换时间 - 借助hashmap, 只走一次遍历 --> O(n)
    def twoSum_4(self, nums, target):
        M = {}
        for idx, x in enumerate(nums):
            sub = target - x
            if sub in M:
                return [M[sub], idx]  # assert idx > M[sub]
            else:
                M[x] = idx
        return []



if __name__ == "__main__":
    nums = [3, 2, 4]
    target = 6
    s = Solution()
    res = s.twoSum_4(nums, target)
    print res

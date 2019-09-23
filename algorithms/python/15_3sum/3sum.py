# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/3sum/

Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.
Note: The solution set must not contain duplicate triplets.

Example:
    Given array nums = [-1, 0, 1, 2, -1, -4],
    A solution set is:
    [
        [-1, 0, 1],
        [-1, -1, 2]
    ]
"""

class Solution(object):

    def threeSum_4(self, nums):
        """
        : 方法4: 
            先排序,再遍历
            三数和为0, 必然有正有负, 即:
                for i < j < k, 以i为左锚点, j=i+1, k=n-1向中间逼近
            由此result不用去重
        : 复杂度 O(n^2) -> received
        """
        res = []
        nums.sort()
        n = len(nums)
        i = 0
        while i < n - 2:
            x = nums[i]
            if x > 0: break  # sum一定非0,提前结束
            j = i + 1
            k = n - 1
            while j < k:
                y = nums[j]
                z = nums[k]
                s = x + y + z
                if s == 0:
                    res.append([x, y, z])
                if s >= 0:
                    while j < k and nums[k] == z:
                        k -= 1  # 右倾k左移(去重)
                if s <= 0:
                    while j < k and nums[j] == y:
                        j += 1  # 左倾i右移(去重)
            while i < n - 2 and nums[i] == x:
                i += 1
        return res

    def threeSum_3(self, nums):
        """
        : 方法3: 
            先排序,再遍历
            三数和为0, 必然有正有负, 即:
                for i < j < k, 以j为锚点 
                    if j <= 0 --> i <= 0 and k >= 0
                    if j >= 0 --> i <= 0 and k >= 0
                    if i + j < 0 -> k 右移
                    if j + k > 0 -> i 左移 
            那么: 遍历时以j为中心向两侧,不满足上述条件及时终止
        : 复杂度: time: O(n^2)
        """
        res = []
        nums.sort()
        n = len(nums)
        for j in range(1, n-1):
            y = nums[j]
            i = j - 1
            k = j + 1
            while i >= 0 and k < n:
                x = nums[i]
                z = nums[k]
                if y >= 0 and x > 0:
                    i -= 1
                    continue
                if y <= 0 and z < 0:
                    k += 1
                    continue
                s = x + y + z
                if s > 0:
                    i -= 1
                elif s < 0:
                    k += 1
                else:
                    new_list = [x, y, z]
                    if new_list not in res:
                        res.append(new_list)
                    i -= 1
                    k += 1
        return res

    def threeSum_2(self, nums):
        """
        :方法2: 在1的基础上,空间换时间
        :      先遍历两个元素的和,然后在后续元素中找满足条件的下标 -> time O(n^2) space O(n) OT
        """
        res = []
        n = len(nums)
        # build map: num -> idx list
        num2idx = {}
        for i in range(0, n):
            x = nums[i]
            if x not in num2idx:
                num2idx[x] = []
            num2idx[x].append(i)
        # iterate
        for i in range(0, n):
            for j in range(i+1, n):
                y = -(nums[i] + nums[j])
                if y not in num2idx:
                    continue
                if not [k for k in num2idx[y] if k not in [i, j]]:
                    continue
                new_list = [nums[i], nums[j], y]
                new_list.sort()
                if new_list in res:
                    continue
                res.append(new_list)
        return res
                

    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :方法1: 直接向后遍历 -> O(n^3) -> OT
        """
        res = []
        n = len(nums)
        for i in range(0, n):
            for j in range(i+1, n):
                sum_2 = nums[i] + nums[j]
                for k in range(j+1, n):
                    if nums[k] != -sum_2:
                        continue
                    new_list = [nums[i], nums[j], nums[k]]
                    new_list.sort()
                    if new_list in res:
                        continue
                    else:
                        res.append(new_list)
        return res

if __name__ == "__main__":
    # nums = [-1, 0, 1, 2, -1, -4]
    # nums = [-1, 0, 0, 0, 0, 0, 0, 1, 2]
    nums = [-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0]
    s = Solution()
    res = s.threeSum_4(nums)
    print res

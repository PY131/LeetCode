# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/4sum/

Given an array nums of n integers and an integer target, 
are there elements a, b, c, and d in nums such that a + b + c + d = target? 
Find all unique quadruplets in the array which gives the sum of target.

Note:
    The solution set must not contain duplicate quadruplets.

Example:
    Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
    A solution set is:
    [
        [-1,  0, 0, 1],
        [-2, -1, 1, 2],
        [-2,  0, 0, 2]
    ]
"""

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        :method:
            - 先对数组进行排序 -> O(nlogn)
            - nums = [o, o, o, o, ..., o, o]
                      |  |  |             |           
                      v  v  v             v           
                      i  j  k1 ->      <- k2
            - loop i, j:
            - sum = nums[i, j, k1, k2]
              if sum == target: yes!! and k1右移 + k2左移
              else if sum < target: k1右移
              else if sum > target: k2左移
        """
        res = []
        dedup_tmp = set()  # 为去重
        n = len(nums)
        nums.sort()
        i = 0
        while i < n - 3:
            j = i + 1
            while j < n - 2:
                k1 = j + 1
                k2 = n - 1
                while k1 < k2:
                    print i, j, k1, k2
                    s = nums[i] + nums[j] + nums[k1] + nums[k2]
                    if s < target:
                        k1 += 1
                    elif s > target:
                        k2 -= 1
                    else:
                        n_l = [nums[i], nums[j], nums[k1], nums[k2]]
                        n_s = ','.join(map(str, n_l))
                        if n_s not in dedup_tmp:
                            dedup_tmp.add(n_s)
                            res.append(n_l)
                        k1 += 1
                        k2 -= 1
                j += 1
            i += 1       
        return res

if __name__ == "__main__":
    nums = [-3,-2,-1,0,0,1,2,3]
    target = 0
    s = Solution()
    res = s.fourSum(nums, target)
    print res

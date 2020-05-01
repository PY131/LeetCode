# coding: utf8
# python 2.7
"""
Given a collection of numbers that might contain duplicates, return all possible unique permutations.
Example:
    Input: [1,1,2]
    Output:
    [
      [1,1,2],
      [1,2,1],
      [2,1,1]
    ]
Link: https://leetcode-cn.com/problems/permutations-ii
"""

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :idea: first sort, then do not search done when repeated happend
        """
        res = []
        nums.sort()
        n = len(nums)
        used = [False] * n

        def help(path):
            if len(path) == n:
                res.append(path[:])
            for i in range(n):
                if used[i] or (i > 0 and nums[i] == nums[i-1] and not used[i-1]):
                    continue
                used[i] = True
                path.append(nums[i])
                help(path)
                path.pop()
                used[i] = False

        help([])
        return res

if __name__ == '__main__':
    so = Solution()
    # nums = [0,1,0,0,9]
    nums = [1,1,2]
    res = so.permuteUnique(nums)
    print res    

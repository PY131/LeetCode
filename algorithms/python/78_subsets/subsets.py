# coding: utf8
# python 2.7
"""
Given a set of distinct integers, nums, return all possible subsets (the power set).
Note: The solution set must not contain duplicate subsets.
Example:
    Input: nums = [1,2,3]
    Output:
    [
      [3],
      [1],
      [2],
      [1,2,3],
      [1,3],
      [2,3],
      [1,2],
      []
    ]
Link: https://leetcode-cn.com/problems/subsets
"""

class Solution(object):

    def subsets(self, nums):
        '''
            using bit to generate all possible combinations
            e.g. 0101 & [4,3,2,1] -> [3,1]
            complexity: time: O(n*2^n), space: O(n*2^n)
        '''
        res = []
        for mask in range(2**len(nums)):
            tmp = []
            j = 0
            while mask:
                if mask % 2:
                    tmp.append(nums[j])
                mask = mask >> 1
                j += 1
            res.append(tmp)
        return res

    def subsets_v3(self, nums):
        '''based on v2, implement by iteration
        '''
        res = [[]]
        n = len(nums)
        for i in range(n):
            res += [it + [nums[i]] for it in res]
        return res

    def subsets_v2(self, nums):
        '''
        the dedup check in method v1 is highly costed
        here we optimize it
        idea: if our searching output is lexicographic, the new item which is inversed can be removed directly
        just as:
                     [ ]
                    / | \
                   /  |  \
                 [1] [2] [3]
                 / |   \
                /  |    \
            [1,2] [1,3] [2,3]
             /
            /
         [1,2,3]
        complexity: time: O(2^n * n), space: O(2^n * n)
        '''
        res = []
        n = len(nums)

        def dfs(idx, path):
            res.append(path[:])
            for i in range(idx, n):
                path.append(nums[i])
                dfs(i+1, path)
                path.pop()
            
        dfs(0, [])
        return res

    def subsets_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # idea: DFS + set dedup based on a map
        # complexity: time O(n*n!*n*logn), space O(n*n!)
        res_m = {'': []}
        n = len(nums)
        nums.sort()
        used = [False] * n
        
        def dfs(path):
            for i in range(n):
                if used[i]:
                    continue
                path.append(nums[i])
                key = ','.join(map(str, sorted(path)))
                if key in res_m:
                    path.pop()
                    continue
                res_m[key] = path[:]
                used[i] = True
                dfs(path)
                used[i] = False
                path.pop()

        dfs([])
        return res_m.values()

if __name__ == '__main__':
    so = Solution()
    nums = [1,2,3]
    res = so.subsets(nums)
    print res

# coding: utf8
# python 2.7
"""
Given a collection of distinct integers, return all possible permutations.
Example:
    Input: [1,2,3]
    Output:
    [
      [1,2,3],
      [1,3,2],
      [2,1,3],
      [2,3,1],
      [3,1,2],
      [3,2,1]
    ]

Link: https://leetcode-cn.com/problems/permutations
"""
class Solution(object):

    def permute_v2(self, nums):
        '''采用一个状态变量来记录当前DFS路径已被使用的元素, 进而不操作原始数据
        '''
        res = []
        N = len(nums)
        used = [False] * N

        def dfs(path):
            if len(path) == N:
                res.append(path[:])
            for i in range(N):
                if not used[i]:
                    used[i] = True
                    path.append(nums[i])
                    dfs(path)
                    used[i] = False
                    path.pop()

        dfs([])
        return res

    def permute(self, nums):
        # 更加规范的DFS-based backtrace
        res = []
        N = len(nums)

        def dfs(idx):
            if idx == N:
                res.append(nums[:])
            for i in range(idx, N):
                nums[idx], nums[i] = nums[i], nums[idx]
                dfs(idx + 1)
                nums[i], nums[idx] = nums[idx], nums[i]

        dfs(0)
        return res

    def permute_v0(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        :idea: using backtrace in recursion
        :complexity: O(n*n!), space: O(n*n!)
        """
        n = len(nums)
        if n < 1:
            return []
        if n < 2:
            return [nums]
        res = []
        for i in range(n):
            sub_nums = nums[:i] + nums[i+1:]
            sub_res = self.permute(sub_nums)
            for x in sub_res:
                res.append([nums[i]] + x)
        return res

if __name__ == '__main__':
    so = Solution()
    nums = [1, 2, 3]
    res = so.permute_v2(nums)
    print res    

# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/partition-equal-subset-sum

Given a non-empty array containing only positive integers, 
find if the array can be partitioned into two subsets such that the sum of elements in both subsets is equal.
 
Example 1:
    Input: [1, 5, 11, 5]
    Output: true
    Explanation: The array can be partitioned as [1, 5, 5] and [11].

Example 2:
    Input: [1, 2, 3, 5]
    Output: false
    Explanation: The array cannot be partitioned into equal sum subsets.
"""

class Solution(object):
    def canPartition(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        S0 = sum(nums)
        if S0 % 2 != 0:
            return False
        S = S0 / 2
        n = len(nums)
        dp = [False] * (S + 1)
        dp[0] = True
        for i in range(1, n+1):
            for j in range(S, 0, -1):
                if nums[i-1] <= j:
                    dp[j] = dp[j] or dp[j - nums[i-1]]
        return dp[S]

if __name__ == "__main__":
    so = Solution()
    print so.canPartition(nums=[1, 5, 11, 5])


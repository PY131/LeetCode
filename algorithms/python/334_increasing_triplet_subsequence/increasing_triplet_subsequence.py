# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/increasing-triplet-subsequence/

Given an unsorted array return whether an increasing subsequence of length 3 exists or not in the array.

Formally the function should:
    Return true if there exists i, j, k
    such that arr[i] < arr[j] < arr[k] given 0 ≤ i < j < k ≤ n-1 else return false.
    Note: Your algorithm should run in O(n) time complexity and O(1) space complexity.

Example 1:
    Input: [1,2,3,4,5]
    Output: true
Example 2:
    Input: [5,4,3,2,1]
    Output: false
"""
class Solution(object):

    def increasingTriplet(self, nums):
        sml = float("+inf")
        mid = float("+inf")
        for x in nums:
            if x <= sml:
                sml = x
            elif x <= mid:
                mid = x
            else:
                return True
        return False

    def increasingTriplet_v2(self, nums):
        # for index = i
        # using p_min[i] = the min number of nums[0: i]
        # using p_max[i] = the max number of nums[i: n)
        # the check if p_min[i-1] < nums[i] < p_max[i+1]
        # complexity: time: O(n), space: O(n)
        n = len(nums)
        if n < 3:
            return False
        p_min = [nums[0]]
        p_max = [nums[n-1]]
        for i in range(1, n):
            j = n - 1 - i
            p_min.append(nums[i] if nums[i] < p_min[-1] else p_min[-1])
            p_max.insert(0, nums[j] if nums[j] > p_max[0] else p_max[0])
        for i in range(1, n-1):
            if p_min[i-1] < nums[i] and nums[i] < p_max[i+1]:
                return True
        return False

    def increasingTriplet_v1(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        # force brute, complexity: time: O(n^3), space: O(1)
        n = len(nums)
        for i in range(n-2):
            for j in range(i+1, n-1):
                if nums[i] >= nums[j]:
                    continue
                for k in range(j+1, n):
                    if nums[j] >= nums[k]:
                        continue
                    return True
        return False

if __name__ == "__main__":
    so = Solution()
    nums = [1,2,3,4,5]
    res = so.increasingTriplet(nums)
    print res

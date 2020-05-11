# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/majority-element-ii
Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
Note: The algorithm should run in linear time and in O(1) space.

Example 1:
    Input: [3,2,3]
    Output: [3]
Example 2:
    Input: [1,1,1,3,3,2,2,2]
    Output: [1,2]
"""

class Solution(object):

    def majorityElement(self, nums):
        # idea: moore vote method
        # time: O(n), space: O(1)

        # 1-st find the biggest two O(n)
        x1, cnt1 = None, 0
        x2, cnt2 = None, 0
        for val in nums:
            if val == x1:
                cnt1 += 1
            elif val == x2:
                cnt2 += 1
            else:
                if cnt1 == 0:
                    x1 = val
                    cnt1 += 1
                elif cnt2 == 0:
                    x2 = val
                    cnt2 += 1
                else:
                    cnt1 -= 1
                    cnt2 -= 1

        # 2-nd count and check O(n)
        cnt1 = 0
        cnt2 = 0
        for val in nums:
            if val == x1:
                cnt1 += 1
            if val == x2:
                cnt2 += 1

        # return
        res = []
        if cnt1 > len(nums) / 3:
            res.append(x1)
        if cnt2 > len(nums) / 3:
            res.append(x2)
        return res

if __name__ == "__main__":
    so = Solution()
    nums = [1,1,1,3,3,2,2,2]
    # nums = [3,2,3]
    res = so.majorityElement(nums)
    print res

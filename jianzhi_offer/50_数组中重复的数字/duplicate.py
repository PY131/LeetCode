# -*- coding:utf-8 -*-
class Solution:
    # 这里要特别注意~找到任意重复的一个值并赋值到duplication[0]
    # 函数返回True/False
    def duplicate(self, numbers, duplication):
        # write code here
        S = set()
        for x in numbers:
            if x not in S:
                S.add(x)
            else:
                duplication[0] = x
                return True
        return False

    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == i:
                i += 1
                continue
            if nums[i] == nums[nums[i]]:
                return nums[i]
            tmp = nums[i]
            nums[i] = nums[nums[i]]
            nums[tmp] = tmp
        return -1

if __name__ == '__main__':
    so = Solution()
    nums = [2, 3, 1, 0, 2, 5, 3]
    res = so.findRepeatNumber(nums)
    print res
class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        if n == 0:
            return
        dp_pos = nums[0]
        dp_neg = nums[0]
        res = dp_pos
        for i in range(1, n):
            dp_pos, \
            dp_neg = \
            max(nums[i], dp_pos * nums[i], dp_neg * nums[i]), \
            min(nums[i], dp_pos * nums[i], dp_neg * nums[i])
            if res < dp_pos:
                res = dp_pos
        return res

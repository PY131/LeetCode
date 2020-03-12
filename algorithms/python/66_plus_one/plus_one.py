# coding: utf8
# python 2.7
"""
@author: Pn
@link: https://leetcode-cn.com/problems/plus-one
@problem_info:    
    Given a non-empty array of digits representing a non-negative integer, 
    plus one to the integer.
    The digits are stored such that the most significant digit is at the head of the list, 
    and each element in the array contain a single digit.

    You may assume the integer does not contain any leading zero, 
    except the number 0 itself.

@example:
    Example 1:
        Input: [1,2,3]
        Output: [1,2,4]
        Explanation: The array represents the integer 123.
    Example 2:
        Input: [4,3,2,1]
        Output: [4,3,2,2]
        Explanation: The array represents the integer 4321.
"""

class Solution(object):

    def plusOne(self, digits):
        """on the base of v3, just add util no add
        """
        if not digits:
            return []
        i = 1
        while i <= len(digits):
            digits[-i] = (digits[-i] + 1) % 10
            if digits[-i] != 0:
                return digits
            else:
                i += 1
        return [1] + digits

    def plusOne_v3(self, digits):
        """based on v2, early stop when add == 0 appears
        """
        if not digits:
            return []
        i = 1
        add = 1
        while i <= len(digits):
            digits[-i] += add
            add, digits[-i] = digits[-i] / 10, digits[-i] % 10
            if add == 0:
                break
            i += 1
        return digits if add == 0 else [1] + digits

    def plusOne_v2(self, digits):
        """just iterative
        """
        if not digits:
            return []
        i = 1
        add = 1
        while i <= len(digits):
            digits[-i] += add
            add, digits[-i] = digits[-i] / 10, digits[-i] % 10
            i += 1
        return digits if add == 0 else [1] + digits

    def plusOne_v1(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        :idea, just simulate the plus operation, using recursion
        """
        def help(digits, i):
            if not i < len(digits):
                return 1
            add = help(digits, i + 1)
            digits[i] += add
            add_new = digits[i] / 10
            digits[i] = digits[i] % 10
            return add_new

        add = help(digits, 0) if digits else 0
        return [1] + digits if add > 0 else digits

if __name__ == '__main__':
    s = Solution()
    nums = [9,9,9]
    res = s.plusOne(nums)
    print res
    

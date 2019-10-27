# coding: utf8
# python 2.7
"""
Determine whether an integer is a palindrome. 
An integer is a palindrome when it reads the same backward as forward.

- Example 1:
    Input: 121
    Output: true
"""
class Solution(object):

    def isPalindrome_3(self, x):
        """
        :method: reverse the num and check if two is equal
        """
        if x < 0:
            return False
        x_old = x
        x_new = 0
        while x_old:
            x_new = x_new * 10 + x_old % 10
            x_old = x_old / 10
        return x == x_new

    def isPalindrome_2(self, x):
        """
        :method: num -> str, no mach different to previous method
        """
        st = str(x)
        n = len(st)
        for i in range(n/2):
            if st[i] != st[n-1-i]:
                return False
        return True

    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        :method: num -> list
            e.g. 121 -> [1, 2, 1] FIFO = FILO
        """
        if x < 0: 
            return False
        digits = []
        n = 0
        while x:
            digits.append(x%10)
            x = x / 10
            n += 1
        for i in range(n/2):
            if digits[i] != digits[n-1-i]:
                return False
        return True

if __name__ == "__main__":
    x = 120
    s = Solution()
    res = s.isPalindrome_3(x)
    print res

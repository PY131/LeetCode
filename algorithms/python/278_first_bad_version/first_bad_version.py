# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/first-bad-version

You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
You are given an API bool isBadVersion(version) which will return whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

Example:

Given n = 5, and version = 4 is the first bad version.

call isBadVersion(3) -> false
call isBadVersion(5) -> true
call isBadVersion(4) -> true

Then 4 is the first bad version.
"""

# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

def isBadVersion(version):
    arr = [0,0,0,1,1,1,1]
    return arr[version-1] == 1
    
class Solution(object):

    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        :idea: just use bi-search, time: O(logn)
        """
        lo = 0
        hi = n - 1
        while lo < hi:
            mi = lo + (hi - lo) / 2
            if isBadVersion(mi+1):
                hi = mi
            else:
                lo = mi + 1
        return lo + 1

if __name__ == "__main__":
    so = Solution()
    res = so.firstBadVersion(7)
    print res

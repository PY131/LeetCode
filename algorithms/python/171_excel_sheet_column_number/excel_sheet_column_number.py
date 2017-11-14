"""
@author: Peng

@Problem_Description:
    Related to question Excel Sheet Column Title
    Given a column title as appear in an Excel sheet, return its corresponding column number.
    
    For example:
        A -> 1
        B -> 2
        C -> 3
        ...
        Z -> 26
        AA -> 27
        AB -> 28 
"""

class Solution(object):
    
    # solution 1
    def titleToNumber_1(self, s):
        """
        :idea: just count by rank
        :type s: str
        :rtype: int
        """
        res = 0
        for i in range(len(s)):
            res = res*26 + (ord(s[i])-ord('A')) + 1
        return res
        
# test code
if __name__ == '__main__':
    s = Solution()
    st = "AABB"
    print('the number of %s is %d.' % (st, s.titleToNumber_1(st)))
    
    
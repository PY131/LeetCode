# coding: utf8
# python 2.7
"""
Given a string containing just the characters:
    '(', ')', '{', '}', '[' and ']', 
determine if the input string is valid.

An input string is valid if:
    Open brackets must be closed by the same type of brackets.
    Open brackets must be closed in the correct order.
Note that an empty string is also considered valid.

link: https://leetcode-cn.com/problems/valid-parentheses
"""

class Solution(object):

    def __init__(self):
        self.left_2_right = {
            '(': ')',
            '{': '}', 
            '[': ']',    
        }

    def isValid(self, s):
        '''using stack (doas python list)
            time:  O(n)
            space: O(n)
        '''
        st = []
        for ch in s:
            if ch in self.left_2_right:
                st.append(ch)
            elif st and ch == self.left_2_right.get(st[-1], ''):
                st.pop()
            else:
                return False
        return len(st) == 0

if __name__ == "__main__":
    so = Solution()
    s = ""
    res = so.isValid(s)
    print s, res

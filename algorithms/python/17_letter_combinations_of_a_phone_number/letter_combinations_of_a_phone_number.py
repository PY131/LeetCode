# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Given a string containing digits from 2-9 inclusive,
    return all possible letter combinations that the number could represent.
    A mapping of digit to letters (just like on the telephone buttons) is given below.
    Note that 1 does not map to any letters.

@example:
    Input: "23"
    Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
"""

digit_2_letters = {
    '2': ['a', 'b', 'c'],
    '3': ['d', 'e', 'f'],
    '4': ['g', 'h', 'i'],
    '5': ['j', 'k', 'l'],
    '6': ['m', 'n', 'o'],
    '7': ['p', 'q', 'r', 's'],
    '8': ['t', 'u', 'v'],
    '9': ['w', 'x', 'y', 'z'],
}

class Solution(object):

    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        :thought: using recursion
            res = letterCombinations[digits[:-1]] x digits[-1]
        """
        res = []
        if not digits:  # boundry
            return res
        letters = digit_2_letters.get(digits[-1], [])  # recursive basis
        res_tmp = self.letterCombinations(digits[:-1])
        if not res_tmp:
            return letters
        if not letters: 
            return res_tmp
        for l in letters:
            res.extend([r + l for r in res_tmp])
        return res

if __name__ == '__main__':
    s = Solution()
    digits = "7"
    res = s.letterCombinations(digits)
    print res
    

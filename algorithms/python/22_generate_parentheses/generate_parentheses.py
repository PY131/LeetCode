"""
@author: Peng

@problem_info:    
    Given n pairs of parentheses, 
    write a function to generate all combinations of well-formed parentheses.

    For example, given n = 3, a solution set is:
        [
          "((()))",
          "(()())",
          "(())()",
          "()(())",
          "()()()"
        ]
"""

class Solution(object):

    def generateParenthesis_2(self, n):
        """
        idea: using dp
            res = '(' + f(p) + ')' + f(q), n = 1 + p + q 
        """
        n2lst = {
            0: [''],
            1: ['()'],
        }
        for m in range(2, n+1):
            new_lst = []
            for p in range(m):
                lst1 = ['(' + l + ')' for l in n2lst[p]]
                q = m - 1 - p
                for l2 in n2lst[q]:
                    new_lst.extend([l1 + l2 for l1 in lst1])
            n2lst[m] = new_lst
        return n2lst[n]

    def generateParenthesis_1(self, n):
        """
        :idea: using recursion
            in a state, we can print n_l '(' (n_l is the number of '(')
                                     n_r ')' (n_r is the number of ')')
            so set str <- str + generate(n_l, n_r);
                  
        :type n: int
        :rtype: List[str]
        """
        lst = []
        st = ''
        self.generate(n, n, st, lst)
        return lst
    
    # helper function of generateParenthesis_1
    def generate(self, n_l, n_r, st, lst):
        """
        :attention: recursion function of solution 1
        
        :param n_l: int, the number of '(' left at current
        :param n_r: int, the number of ')' left at current
        :param st:  str, the string head of previous generation
        :param lst: list, for storing all possible parenthesis string (act as return)
        """
        if n_l == 0 and n_r == 0 : 
            lst.append(st)
            return
        if n_l > 0:
            self.generate(n_l-1, n_r, st+'(', lst)
        if n_r > 0 and n_r > n_l:  # ')' appear only if there exist '(' in the left (mean n_r > n_l)
            self.generate(n_l, n_r-1, st+')', lst)

# test code
if __name__ == '__main__':
    s = Solution()
    n = 3
    print("all possible parenthesis sequences are:")
    lst1 = s.generateParenthesis_1(n)
    lst2 = s.generateParenthesis_2(n)
    print(lst1)
    print(lst2)

# - PY131 - #
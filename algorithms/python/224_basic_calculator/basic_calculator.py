"""
@author: PENG

@Problem:
    Implement a basic calculator to evaluate a simple expression string.

    The expression string may contain open ( and closing parentheses ), 
    the plus + or minus sign -, non-negative integers and empty spaces .
    
    You may assume that the given expression is always valid.
    
    Some examples:
        "1 + 1" = 2
        " 2-1 + 2 " = 3
        "(1+(4+5+2)-3)+(6+8)" = 23
    
    Note: 
    Do not use the eval built-in library function.
"""

class Solution(object):
    
    """
    Solution 1
        idea:
        use two stacks:
            stack 1: store numbers to be computed.
            stack 2: store operators to be computed.
        thought scanning:
            compare the priority between (next operator) and (top operator in stack 2)
            and make different operation.
    """
    def calculate(self, s):
        """
        :param s: str, expression
        :return: int, calculate's result
        """
        # constructing priority matrix (using dictionary)
        #    |  (  )  +  -  .
        # -------------------
        #  ( |  <  =  <  <  >
        #  ) |  =  >  <  <  >
        #  + |  <  >  >  >  >
        #  - |  <  >  >  >  >
        #  . |  <  <  <  <  =
        oper_pri = {'(': {'(': '<', ')': '=', '+': '<', '-': '<', '.': '>'},
                    ')': {'(': '=', ')': '>', '+': '<', '-': '<', '.': '>'},
                    '+': {'(': '<', ')': '>', '+': '>', '-': '>', '.': '>'},
                    '-': {'(': '<', ')': '>', '+': '>', '-': '>', '.': '>'},
                    '.': {'(': '<', ')': '<', '+': '<', '-': '<', '.': '='}}

        st_nb = []  # use list as stack
        st_op = ['.'] 
        s += '.'  # add '.' as ending character
        flag = False
        i = 0
        while i < len(s):
            ch = s[i]
            # number
            if ch.isdigit(): 
                if flag == False: 
                    st_nb.append( int(ch) )
                    flag = True
                else: # continuous digit
                    st_nb.append( st_nb.pop()*10  + int(ch) )
            # space
            elif ch == " ": 
                flag = False
            # operator
            else: 
                flag = False
                if len(st_op) == 0 or oper_pri[st_op[-1]][ch] == '<' : # new operator has a higher priority 
                    st_op.append(ch)
                elif len(st_op) == 0 or oper_pri[st_op[-1]][ch] == '=' : # new operator has a same priority 
                    st_op.pop()
                else: 
                    n1 = st_nb.pop()  # here all the binary operator
                    n2 = st_nb.pop()
                    op = st_op.pop()
                    st_nb.append(self.calcu(n2, op, n1))
                    i -= 1
            i += 1
            
        # return the result                
        return st_nb[0]
    
    # helper function for solution 1 to do a calculation         
    def calcu(self, num1, oper, num2):
        if oper == "+": return num1 + num2
        if oper == "-": return num1 - num2
        
# test code
if __name__ == '__main__':
    s = Solution()
    expr = "2+3-21"
    res = s.calculate(expr)
    print(res)

print(" - PY131 - ")
"""
@author: PENG

@Problem:
    Implement a basic calculator to evaluate a simple expression string.
    The expression string contains only non-negative integers, +, -, *, / operators 
    and empty spaces . The integer division should truncate toward zero.

    You may assume that the given expression is always valid.

    Some examples:
        "3+2*2" = 7
        " 3/2 " = 1
        " 3+5 / 2 " = 5
    Note: Do not use the eval built-in library function.
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
        oper_pri = {'.': 0, '+':1, '-':1, '*':2, '/':2 }  # a simple priority level of related operation
        st_nb = []  # use list as stack
        st_op = [] 
        s += '.'  # add '.' as ending character
        flag = False
        for ch in s:
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
                continue
            # operator
            else: 
                flag = False
                if len(st_op) == 0 or oper_pri[st_op[-1]] < oper_pri[ch]: # new operator has a higher priority 
                    st_op.append(ch)
                else: # calculate current highest priority part
                    while len(st_op) != 0 and oper_pri[st_op[-1]] >= oper_pri[ch] :
                        n1 = st_nb.pop()  # here all the binary operator
                        n2 = st_nb.pop()
                        op = st_op.pop()
                        
                        st_nb.append(self.calcu(n2, op, n1)) 
                    st_op.append(ch)
        # return the result                
        return st_nb[0]
    
    # helper function for solution 1 to do a calculation         
    def calcu(self, num1, oper, num2):
        if oper == "+": return num1 + num2
        if oper == "-": return num1 - num2
        if oper == "*": return num1 * num2
        if oper == "/": return int(num1 / num2)
        
        
# test code
if __name__ == '__main__':
    s = Solution()
    expr = "3  + 2 * 5/6"
    res = s.calculate(expr)
    print(res)
    # print("%s = %d" % (expr, res))

print(" - PY131 - ")
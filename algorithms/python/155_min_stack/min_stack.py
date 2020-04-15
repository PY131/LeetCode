# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/min-stack

Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
    MinStack minStack = new MinStack();
    minStack.push(-2);
    minStack.push(0);
    minStack.push(-3);
    minStack.getMin();   --> Returns -3.
    minStack.pop();
    minStack.top();      --> Returns 0.
    minStack.getMin();   --> Returns -2.
"""
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A = []

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.A.append(x)

    def pop(self):
        """
        :rtype: None
        """
        return self.A.pop()

    def top(self):
        """
        :rtype: int
        """
        return self.A[-1]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.A)

if __name__ == "__main__":
    obj = MinStack()
    obj.push(-2)
    print obj.A

    obj.push(0)
    print obj.A

    obj.push(-3)
    print obj.A

    print obj.getMin()
    print obj.A

    print obj.pop()
    print obj.A

    print obj.top()
    print obj.A

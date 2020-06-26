# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.stack = []
        self.stack_2 = []
    
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.stack_2 and node > self.stack_2[-1]:
            self.stack_2.append(self.stack_2[-1])
        else:
            self.stack_2.append(node)
        
    def pop(self):
        # write code here
        self.stack_2.pop()
        return self.stack.pop()
        
    def top(self):
        # write code here
        return self.stack[-1]
        
    def min(self):
        # write code here
        return self.stack_2[-1]
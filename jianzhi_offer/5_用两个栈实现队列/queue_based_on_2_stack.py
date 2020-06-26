# -*- coding:utf-8 -*-
class Solution:
    def __init__(self):
        self.st1 = []
        self.st2 = []
        
    def push(self, node):
        # write code here
        self.st1.append(node)
        
    def pop(self):
        # return xx
        if not self.st2:
            while self.st1:
                self.st2.append(self.st1.pop())
        return self.st2.pop()

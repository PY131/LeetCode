# coding: utf8
# python 2.7

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class LinkedList(object):

    def __init__(self, arr=[]):
        self.size = len(arr)
        self.head = self.build_a_list(arr)
    
    def build_a_list(self, arr):
        p = pivot = ListNode(-1)
        for v in arr:
            p.next = ListNode(v)
        return pivot.next

# test code
if __name__ == '__main__':
    arr = [1,2,3,4]

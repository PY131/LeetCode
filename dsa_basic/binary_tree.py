# -*- coding: utf-8 -*-

class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinTree(object):

    def rebuild_a_tree(self, pres, ins):
        


if __name__ == "__main__":
    # generate a tree by pre and in order array
    pre_orders = []
    in_orders = []
    BT = BinTree()

    root = BT.rebuild_a_tree(pre_orders, in_orders)

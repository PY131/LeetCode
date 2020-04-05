# coding: utf8
# python 2.7

class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class BTreeHelper(object):

    def build_a_tree(self, arr=[]):
        # 建节点
        N = len(arr)
        node_arr = [TreeNode(val) if val else None for val in arr]
        # 建边
        for i in range(N):
            if node_arr[i]:
                i_l = 2 * i + 1
                i_r = 2 * i + 2
                if i_l < N:
                    node_arr[i].left = node_arr[i_l]
                if i_r < N:
                    node_arr[i].right = node_arr[i_r]
        # root
        return node_arr[0]

    def trav_pre(self, x):
        '''子树的先序遍历(递归版)
        '''
        if not x:
            return
        print x.val,
        self.trav_pre(x.left)
        self.trav_pre(x.right)

# test code
if __name__ == '__main__':
    BT = BTreeHelper()
    arr = [3,9,20,None,None,15,7]
    root = BT.build_a_tree(arr)

    # print
    BT.trav_pre(root)

# -*- coding: utf-8 -*-

class TreeNode(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinTree(object):

    def rebuild_a_tree(self, pres, ins):

        def find(nums, tar):
            # find the index of node val in nums[lo, hi]
            for i in range(len(nums)):
                if nums[i] == tar:
                    return i
            return -1

        def build(nums1, nums2):
            if (not nums1) or (not nums2):
                return None
            root = TreeNode(nums1[0])
            idx = find(nums2, nums1[0])
            root.left = build(nums1[1: idx+1], nums2[0: idx])
            root.right = build(nums1[idx+1:], nums2[idx+1:])
            return root

        root = build(pres, ins)
        return root

    def level_traversal(self, root):
        res = []
        res_node = []
        tmp = [root]
        while tmp:
            tmp_new = []
            for node in tmp:
                if node:
                    res.append(node.val)
                    res_node.append(node)
                    tmp_new.extend([node.left, node.right])
            tmp = tmp_new
        return res, res_node

    def preorder_traversal(self, root, method="iterative"):
        res = []

        def help_v1(root):
            if not root:
                return
            res.append(root.val)
            help_v1(root.left)
            help_v1(root.right)

        def help_v2(root):
            S = [root] if root else []
            while S:
                p = S.pop()
                res.append(p.val)
                if p.right:
                    S.append(p.right)
                if p.left:
                    S.append(p.left)

        if method == "recursive":
            help_v1(root)
        else:
            help_v2(root)
        return res

    def inorder_traversal(self, root, method="iterative"):
        res = []

        def help_v1(root):
            if not root:
                return
            help_v1(root.left)
            res.append(root.val)
            help_v1(root.right)

        def help_v2(root):
            S = []

            def go_along_left_branch(p):
                while p:
                    S.append(p)
                    p = p.left
            p = root
            while True:
                go_along_left_branch(p)
                if not S:
                    break
                p = S.pop()
                res.append(p.val)
                p = p.right

        if method == "recursive":
            help_v1(root)
        else:
            help_v2(root)
        return res

    def postorder_traversal(self, root, method="iterative"):
        res = []

        def help_v1(root):
            if not root:
                return
            help_v1(root.left)
            help_v1(root.right)
            res.append(root.val)

        def help_v2(root):
            S = [root] if root else []
            tmp = []
            while S:
                p = S.pop()
                tmp.append(p.val)
                if p.left:
                    S.append(p.left)
                if p.right:
                    S.append(p.right)
            for i in range(len(tmp) - 1, -1, -1):
                res.append(tmp[i])

        if method == "recursive":
            help_v1(root)
        else:
            help_v2(root)
        return res

    def mirror(self, root):
        if root:
            tmp = root.left
            root.left = self.mirror(root.right)
            root.right = self.mirror(tmp)
        return root

    def lowest_common_root(self, root, node1, node2):
        if not root or root == node1 or root == node2:
            return root
        l = self.lowest_common_root(root.left, node1, node2)
        r = self.lowest_common_root(root.right, node1, node2)
        if not l:
            return r
        if not r:
            return l
        return root

if __name__ == "__main__":
    # generate a tree by pre and in order array
    preorder = [0,1,3,4,7,8,10,2,5,6,9]
    inorder = [3,1,7,4,10,8,0,5,2,6,9]
    BT = BinTree()

    root = BT.rebuild_a_tree(preorder, inorder)
    print root
    res, res_node = BT.level_traversal(root)
    print "level traversal: ", res

    if False:
        res = BT.preorder_traversal(root, method='recursive')
        print "preorder traversal recursively: ", res
        res = BT.preorder_traversal(root, method='iterative')
        print "preorder traversal iteritively: ", res

        res = BT.inorder_traversal(root, method='recursive')
        print "inorder traversal recursively: ", res
        res = BT.inorder_traversal(root, method='iterative')
        print "inorder traversal iteritively: ", res

        res = BT.postorder_traversal(root, method='recursive')
        print "postorder traversal recursively: ", res
        res = BT.postorder_traversal(root, method='iterative')
        print "postorder traversal iteritively: ", res

    # mirror of BinTree
    if False:
        root = BT.mirror(root)
        res = BT.level_traversal(root)
        print "after mirroring, level traversal: ", res

    # lowest common root of two node in tree
    if True:
        node1, node2 = res_node[3], res_node[7]
        res = BT.lowest_common_root(root, node1, node2)
        print "lowest common root %s, %s of is %s " % (node1.val, node2.val, res.val)

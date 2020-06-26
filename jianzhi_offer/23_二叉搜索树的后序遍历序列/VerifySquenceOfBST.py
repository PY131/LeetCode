# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        def find_idx(arr, lo, hi, tar):
            # 判断在arr的[lo, hi]区间不小于tar的最小下标，没有找到返回hi+1
            i = lo
            while i <= hi:
                if arr[i] < tar:
                    i += 1
                    continue
                else:
                    break
            return i

        def check(arr, lo, hi):
            # 判断arr在[lo, hi]之间是否构成BST的后序遍历
            flag = True
            if not lo < hi:
                return flag
            root_val = arr[hi]
            root_idx = find_idx(arr, lo, hi - 1, root_val)
            if lo < root_idx:  # 存在左子树
                if root_val > max(arr[lo: root_idx]):
                    flag = flag and check(arr, lo, root_idx - 1)
                else:
                    return False
            if root_idx < hi:  # 存在右子树
                if root_val < min(arr[root_idx: hi]):
                    flag = flag and check(arr, root_idx, hi - 1)
                else:
                    return False
            return flag

        if not sequence:
            return False
        return check(sequence, 0, len(sequence) - 1)
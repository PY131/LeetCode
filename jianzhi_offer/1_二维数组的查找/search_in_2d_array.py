# coding: utf8
# python 2.7

class Solution:

    # 采用二分查找，O(m*lgn)

    def Find(self, target, array):
        m = len(array)
        n = len(array[0]) if m > 0  else 0
        if m == 0 or n == 0:
            return False
        for i in range(m):
            if target < array[i][0] or target > array[i][n-1]:
                continue
            if self.bi_search(target, array[i], 0, n-1):
                return True
        return False

    def bi_search(self, tar, arr, lo, hi):
        while lo <= hi:
            mi = (lo + hi) / 2
            if tar == arr[mi]:
                return True
            elif tar < arr[mi]:
                hi = mi - 1
            else:
                lo = mi + 1
            return self.bi_search(tar, arr, lo, hi)
        return False

    def Find_v2(self, target, array):
        # another solution
        m = len(array)
        n = len(array[0]) if m > 0  else 0
        i = 0
        j = n - 1
        while i < m and j >= 0:
            if array[i][j] == target:
                return True
            elif array[i][j] > target:
                j -= 1
            else:
                i += 1
        return False

if __name__ == "__main__":
    array = [[1,2,3],[2,3,4],[3,4,5]]
    target = 6
    s = Solution()
    res = s.Find(target, array)
    print res

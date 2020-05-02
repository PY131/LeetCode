# coding: utf8
# python 2.7

class PriorityQueueNew(object):

    def __init__(self, arr=[]):
        self.size = 0
        self.H = []  # format as [<k1, v1>, <k2, v2>, ...]
        # 初始化堆
        if arr:
            self._build(arr)

    def _build(self, arr):
        self.size = len(arr)
        self.H = arr[:]
        for i in range(self.size / 2 - 1, -1, -1):  # 建堆, 从第一个非叶子节点往上
            self._adjust(i)

    def _swap(self, i, j):
        self.H[i], self.H[j] = self.H[j], self.H[i]

    def _adjust(self, i):
        # 从第i个节点开始下滤
        while i < self.size:
            k = l = 2*i+1
            r = l+1
            if r < self.size and self.H[r][0] < self.H[l][0]:
                k = r
            if k < self.size and self.H[k][0] < self.H[i][0]:
                self._swap(k, i)
            i = k

    def put(self, item):
        self.size += 1
        self.H.append(item)
        for i in range(self.size / 2 - 1, -1, -1):
            self._adjust(i)

    def top(self):
        return self.H[0]

    def pop(self):
        if not self.size:
            return None
        self.size -= 1
        self._swap(-1, 0)
        res = self.H.pop()
        self._adjust(0)
        return res

# test code
if __name__ == '__main__':
    pq = PriorityQueueNew()
    nums = [3,1,2,4]
    for x in nums:
        pq.put((x, x))
        print pq.H
    k = len(nums)
    while k:
        print pq.pop()[1]
        k -= 1

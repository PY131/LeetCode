# -*- coding: utf-8 -*-

class SlidingWindow(object):

    def length_of_longest_substring_with_no_repeat(self, s):
        # 字符串中，无重复字符的最长子串长度
        res = 0
        n = len(s)
        M = {}
        i = j = 0
        while j < n:
            c = s[j]
            if c in M:
                if res < j - i:
                    res = j - i
                tmp = M[c] + 1
                while i < tmp:
                    M.pop(s[i])
                    i += 1
            M[c] = j
            j += 1
        if res < j - i:
            res = j - i
        return res

    def max_sliding_window(self, nums, k):
        '''
        滑动窗口(size=k)的最大值
        e.g:
            输入: nums = [1,3,-1,-3,5,3,6,7], 和 k = 3
            输出: [3,3,5,5,6,7] 
            解释: 

              滑动窗口的位置                最大值
            ---------------               -----
            [1  3  -1] -3  5  3  6  7       3
             1 [3  -1  -3] 5  3  6  7       3
             1  3 [-1  -3  5] 3  6  7       5
             1  3  -1 [-3  5  3] 6  7       5
             1  3  -1  -3 [5  3  6] 7       6
             1  3  -1  -3  5 [3  6  7]      7
        '''
        res = []
        if not nums:
            return res
        n = len(nums)
        # assert 1 <= k <= n
        sw = []
        for i in range(k):
            while sw:
                if nums[i] <= nums[sw[-1]]:
                    break
                sw.pop()
            sw.append(i)

        for i in range(k, n):
            res.append(nums[sw[0]])
            if i - k == sw[0]:
                sw.pop(0)
            while sw:
                if nums[i] <= nums[sw[-1]]:
                    break
                sw.pop()
            sw.append(i)

        res.append(nums[sw[0]])
        return res

    def min_window(self, s, t):
        # 字符串s中包含字符串t的最小字串
        

if __name__ == "__main__":
    SW = SlidingWindow()

    if False:
        s = "abba"
        print SW.length_of_longest_substring_with_no_repeat(s)
    
    if False:
        print SW.max_sliding_window(nums=[7,2,4], k=2)

    if False:
        print SW.max_sliding_window(S="ADOBECODEBANC", T="ABC")
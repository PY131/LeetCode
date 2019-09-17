# coding: utf8
# python 2.7
"""
https://leetcode-cn.com/problems/container-with-most-water/
"""

class Solution(object):

    def maxArea_3(self, height):
        """
        :方法3: 方法2提供了一种从2边向中间靠近的思路    
            进一步分析,
            - 对于最初的两边hi, hj 其间weight是所有可能组合中最大的
            - 所以,要在i,j之间找到更优,必须是new_h>min(hi, hj)
            - 所以: 
                hi < hj -> i++
                hi > hj -> j--
                hi = hj -> i++, j--
            - 由此-->O(n)
        """
        res = 0
        n = len(height)
        hei_max = 0
        i, j = 0, n - 1
        while i < j:
            hei = min(height[i], height[j])
            if hei > hei_max:
                hei_max = hei
                area = hei * (j - i)
                if area > res:
                    res = area
            if height[i] < height[j]:
                i += 1
            elif height[i] > height[j]:
                j -= 1
            else:
                i += 1
                j -= 1
        return res

    def maxArea_2(self, height):
        """
        :method 2, 在method 1基础上: 
            改进:从两端向中间遍历,直接抛弃lenght小的 -> O(n^2) 依然out of time limit
        """
        res = 0
        n = len(height)
        len_max = 0
        for i in range(n):
            for j in range(n-1, i, -1):
                length = min(height[i], height[j])
                if length <= len_max:
                    continue
                len_max = length
                weight = j - i
                area = length * weight
                if area > res:
                    res = area
        return res

    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        :method 1: force, iterate two line with length O(n^2)-> out of time
        """
        res = 0
        n = len(height)
        for i in range(n):
            for j in range(i+1, n):
                length = min(height[i], height[j])
                weight = j - i
                area = length * weight
                if area > res:
                    res = area
        return res

if __name__ == "__main__":
    h = [1,8,6,2,5,4,8,3,7]
    s = Solution()
    res = s.maxArea_3(h)
    print res

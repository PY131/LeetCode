# coding: utf8
# python 2.7
"""
- Problem:
    There are two sorted arrays nums1 and nums2 of size m and n respectively.                                   11      e3          
    Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
    You may assume nums1 and nums2 cannot be both empty.

- Example:
    nums1 = [1, 3]
    nums2 = [2]
    The median is 2.0
"""

class Solution(object):

    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        :method: 
            consider the complexity oughts to be under O(lg(m+n)),
            using bi-search after finding out the median number's condition
        """
        res = 0.0
        len1 = len(nums1)
        len2 = len(nums2)
        if len1 <= len2:
            a = nums1  # using a refers to the shorter array and b refers to the longer one
            b = nums2
            m = len1
            n = len2
        else:
            a = nums2
            b = nums1
            m = len2
            n = len1
        i_min = 0
        i_max = m
        while i_min <= i_max:
            # bin-search i in [i_min, i_max]
            i = (i_min + i_max) / 2
            j = (m + n + 1) / 2 - i
            if i > i_min and j < n and a[i-1] > b[j]:
                i_max = i - 1
            elif i < i_max and j > 0 and b[j-1] > a[i]:
                i_min = i + 1
            else:  # hit res when
                left_max = 0
                right_min = 0
                if i == 0:
                    left_max = b[j-1]
                elif j == 0:
                    left_max = a[i-1]
                else:
                    left_max = max(a[i-1], b[j-1])
                if (m + n) % 2 != 0:  # even
                    res = left_max
                else: 
                    if i == m:
                        right_min = b[j]
                    elif j == n:
                        right_min = a[i]
                    else:
                        right_min = min(a[i], b[j])
                    res = 1.0 * (left_max + right_min) / 2
                break
        return res

    def findMedianSortedArrays_v1(self, nums1, nums2):
        '''using merge sort
        '''
        m = len(nums1)
        n = len(nums2)
        i = 0
        j = 0
        tmp = []
        while i < m and j < n:
            if nums1[i] <= nums2[j]:
                tmp.append(nums1[i])
                i += 1
            else:
                tmp.append(nums2[j])
                j += 1
        while i < m:
            tmp.append(nums1[i])
            i += 1
        while j < n:
            tmp.append(nums2[j])
            j += 1
        if (m + n) % 2 == 1:
            res = tmp[(m+n)/2]
        else:
            res = ( tmp[(m+n)/2] + tmp[(m+n-1)/2] ) / 2.0
        return res
    
    def findMedianSortedArrays_v2(self, nums1, nums2):
        '''using bin search
        '''
        m = len(nums1)
        n = len(nums2)
        if m > n:
            nums1, nums2 = nums2, nums1
            m, n = n, m
        n_left = (m + n + 1) / 2
        lo = 0
        hi = m
        while lo < hi:
            i = (lo + hi + 1) / 2
            j = n_left - i
            if nums1[i - 1] > nums2[j]:
                hi = i - 1
            else:
                lo = i
        i = lo
        j = n_left - lo
        left_1 = nums1[i-1] if i > 0 else float("-inf")
        left_2 = nums2[j-1] if j > 0 else float("-inf")
        right_1 = nums1[i] if i < m else float("+inf")
        right_2 = nums2[j] if j < n else float("+inf")
        if (m + n) % 2 == 1:
            return max(left_1, left_2)
        else:
            return (max(left_1, left_2) + min(right_1, right_2)) / 2.0

if __name__ == "__main__":
    nums1 = [1, 3, 5]
    nums2 = [2, 4]
    s = Solution()
    res = s.findMedianSortedArrays_v2(nums1, nums2)
    print res

# coding: utf8
# python 2.7
"""
@author: Pn
@problem_info:    
    Write a function to find the longest common prefix string amongst an array of strings.
    If there is no common prefix, return an empty string "".
    p.s.All given inputs are in lowercase letters a-z.

@example:
    Input: ["flower","flow","flight"]
    Output: "fl"
"""

class Solution(object):

    def longestCommonPrefix_2(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :thought: 
            think of previous method, we have wasted some time to those chars that will certainly be removed later
            so.
            here we just iterative epoch by epoch,
            1-st: check the 1-st char of each strs
            2-nd: check the 2-en char of each strs
            once not equal for all, return
        """
        cnt = 0
        flag = True if strs else False
        while flag:
            if len(strs[0]) <= cnt:
                flag = False
            else:
                for st in strs[1:]:
                    if len(st) <= cnt or st[cnt] != strs[0][cnt]:
                        flag = False
            if flag:
                cnt += 1
        return strs[0][0:cnt] if strs else ""

    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        :thought: just iterative and reserve current longest-common-prefix
        """
        num = len(strs)
        res = strs[0] if num > 0 else ""
        cnt = len(res)
        for i in range(1, num):
            # get common predix between res and current str
            cnt_tmp = len(strs[i]) if len(strs[i]) < cnt else cnt
            j = 0
            while j < cnt_tmp:
                if strs[i][j] != res[j]:
                    break
                j += 1
            cnt = j
            res = res[0: j]
        return res

if __name__ == '__main__':
    s = Solution()
    strs = ["dog","docecar","dar"]
    res = s.longestCommonPrefix_2(strs)
    print res
    

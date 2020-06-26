# coding: utf8
# python 2.7
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        n = len(s)
        for i in range(n):
            if s[i] == ' ':
                s += '  '
        j = len(s) - 1
        for i in range(n-1, -1, -1):
            if s[i] == ' ':
                s[j] = '0'
                s[j-1] = '2'
                s[j-2] = '%'
                j -= 3
            else:
                s[j] = s[i]
        return s

if __name__ == "__main__":
    st = "hello world"
    s = Solution()
    res = s.replaceSpace(st)
    print res

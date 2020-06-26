# -*- coding:utf-8 -*-
class Solution:
    def ReverseSentence(self, s):
        # write code here
        st = []
        tmp = ''
        for x in s:
            if x == ' ':
                st.append(tmp)
                tmp = ''
            else:
                tmp += x
        if tmp:
            st.append(tmp)
        res = ''
        while st:
            res += st.pop()
            if st:
                res += ' '
        return res

if __name__ == '__main__':
    s = 'student. a am I'
    so = Solution()
    res = so.ReverseSentence(s)
    print res
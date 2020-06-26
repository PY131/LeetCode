# -*- coding:utf-8 -*-
class Solution:
    def PrintMinNumber(self, numbers):
        # write code here -- O(n^2)
        s = []
        k = 0
        for x in numbers:
            i = 0
            while i < k:
                if str(x) + s[i] <= s[i] + str(x):
                    break
                i += 1
            s.insert(i, str(x))
            k += 1
        return ''.join(s)

    def PrintMinNumber_2(self, numbers):
        # write code here
        def cmp_2(a, b):
            # return True if a <= b in current context
            x1 = str(a) + str(b)
            x2 = str(b) + str(a)
            if x1 > x2:
                return 1
            elif x1 < x2:
                return -1
            return 0
            
        res = sorted(numbers, cmp=cmp_2)
        return ''.join(map(str, res))

if __name__ == '__main__':
    arr = [4,5,1,6,2,7,3,8]
    so = Solution()
    res = so.PrintMinNumber_2(arr)
    print res
# -*- coding:utf-8 -*-
class Solution:
    def jumpFloor(self, number):
        # write code here
        i = 2
        p0 = p1 = 1
        while i <= number:
            p1 = p1 + p0
            p0 = p1 - p0
            i += 1
        return p1

    def throwCoins(self, number):
        f_up = 1
        f_down = 1
        i = 2
        while i <= number:
            tmp = f_up
            f_up = f_down
            f_down = tmp + f_down
            i += 1
        return f_down + f_up


    def throwCoins(self, number):
        f_up[1] = 1
        f_down[1] = 1
        i = 2
        while i <= number:
            f_up[i] = f_down[i-1]
            f_down[i] = f_up[i-1] + f_down[i-1]
            i += 1
        return f_down[number] + f_up[number]

if __name__ == '__main__':
    num = 10
    so = Solution()
    print so.throwCoins(num)
# -*- coding:utf-8 -*-
class Solution:
    def Permutation(self, ss):
        # write code here
        if not ss:
            return []
        res = []
        c = list(ss)
        
        def dfs(i):
            if i == len(c)-1:
                res.append(''.join(c))
                return
            d = set()
            for j in range(i, len(c)):
                if c[j] in d:
                    continue
                d.add(c[j])
                c[i], c[j] = c[j], c[i]
                dfs(i+1)
                c[i], c[j] = c[j], c[i]
        
        dfs(0)
        return res
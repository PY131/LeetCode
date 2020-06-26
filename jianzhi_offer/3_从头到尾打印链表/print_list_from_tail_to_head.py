# coding: utf8
# python 2.7
from ..self_made_libs.linked_list in LinkedList

class Solution:

    def printListFromTailToHead(self, s):
        # using list.insert function
        res = []
        p = listNode
        while p:
            res.insert(0, p.val)
            p = p.next
        return res

if __name__ == "__main__":
    arr = [1,2,3,4,5]
    l = LinkedList(arr)
    s = Solution()
    res = s.printListFromTailToHead(l)
    print res

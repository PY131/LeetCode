# coding: utf8
# python 2.7

class ListNode(object):
    def __init__(self, k, v):
        self.key = k
        self.val = v
        self.pre = None
        self.suc = None

class DoubleLinkedList(object):
    def __init__(self):
        self.size = 0
        self.head = ListNode(-1, -1)
        self.tail = ListNode(-1, -1)
        self.head.suc = self.tail
        self.tail.pre = self.head

    def add(self, k, v):
        tmp = ListNode(k, v)
        tmp.pre = self.head
        tmp.suc = self.head.suc
        tmp.suc.pre = tmp
        tmp.pre.suc = tmp
        self.size += 1
        return tmp
    
    def pop(self):
        if self.size == 0:
            return None
        tmp = self.tail.pre
        tmp.pre.suc = self.tail
        self.tail.pre = tmp.pre
        self.size -= 1
        return tmp
    
    def get(self):
        if self.size == 0:
            return None
        return self.head.suc.val

    def remove(self, node):
        # assert node in list
        node.pre.suc = node.suc
        node.suc.pre = node.pre
        self.size -= 1

class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.capacity = capacity
        self.L = DoubleLinkedList()
        self.M = {}

    def get(self, key):
        """
        :type key: int
        :rtype: int
        """
        print "before get %s" % key
        print self.M
        if key not in self.M:
            return -1
        node = self.M[key]
        self.L.remove(node)
        self.L.add(node.key, node.val)
        return node.val

    def put(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: None
        """
        if key in self.M:
            node = self.M[key]
            self.L.remove(node)
            new_node = self.L.add(key, value)
            self.M[key] = new_node
        else:
            if self.L.size == self.capacity:
                node = self.L.pop()
                self.M.pop(node.key)
            new_node = self.L.add(key, value)
            self.M[key] = new_node
        
if __name__ == '__main__':

    obj = LRUCache(2)
    obj.put(1, 1)
    obj.put(2, 2)
    print obj.get(1)
    obj.put(3, 3)
    print obj.get(2)
    obj.put(4, 4)
    print obj.get(1)
    print obj.get(3)
    print obj.get(4)

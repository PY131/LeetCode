# -*- coding: utf-8 -*-

import random

class Node(object):
    def __init__(self, val):
        self.val = val
        self.next = None

class LinkedList(object):

    def build_a_list(self, array):
        pivot = pre = Node(-1)
        for val in array:
            cur = Node(val)
            pre.next = cur
            pre = pre.next
        return pivot.next

    def to_array(self, head):
        res = []
        p = head
        while p:
            res.append(p.val)
            p = p.next
        return res

    def invert(self, head):
        pre = None
        cur = head
        while cur:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre

    def invert_first_k(self, head, k):
        # find the first node for next segment
        p = head
        while k > 0 and p:
            p = p.next
            k -= 1
        pre = p
        cur = head
        while cur and cur != p:
            nxt = cur.next
            cur.next = pre
            pre = cur
            cur = nxt
        return pre, cur

    def invert_k_by_k(self, head, k):
        tail = head
        pre, next_pre = self.invert_first_k(head, k)
        head_new = pre
        while next_pre:
            tmp = next_pre
            pre, next_pre = self.invert_first_k(next_pre, k)
            tail.next = pre
            tail = tmp
        return head_new

    def merge_sort(self, head):

        def find_middle(h):
            # assert head and head.next are both exists
            p1 = h
            p2 = h.next
            while p2 and p2.next:
                p2 = p2.next.next
                p1 = p1.next
            return p1

        def merge_two(h1, h2):
            pre = Node(-1)
            p = pre
            p1 = h1
            p2 = h2
            while p1 and p2:
                if p1.val <= p2.val:
                    p.next = p1
                    p = p1
                    p1 = p1.next
                else:
                    p.next = p2
                    p = p2
                    p2 = p2.next
            while p1:
                p.next = p1
                p = p1
                p1 = p1.next
            while p2:
                p.next = p2
                p = p2
                p2 = p2.next
            return pre.next

        def partition_sort_merge(h):
            if (not h) or (not h.next):
                return h
            tmp = find_middle(h)
            h2 = tmp.next
            tmp.next = None
            h1_new = partition_sort_merge(h)
            h2_new = partition_sort_merge(h2)
            h_new = merge_two(h1_new, h2_new)
            return h_new

        return partition_sort_merge(head)

    def delete_kth_from_end(self, head, k):
        pre = Node(-1)
        pre.next = head
        p1 = p2 = pre
        # find the k+1 th node from the end
        while p1:
            p1 = p1.next
            if k >= 0:
                k -= 1
            else:
                p2 = p2.next
        # delete target node and return
        tar = p2.next
        if tar:
            p2.next = p2.next.next
        return pre.next, tar

if __name__ == "__main__":
    # generate random array list
    raw_list = []
    for _ in range(10):
        raw_list.append(random.randint(0, 1000000))

    L = LinkedList()

    # revert the list
    if False:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new = L.invert(head)
        print "after:", L.to_array(head_new)

    # revert the first k item in list
    if False:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new, _ = L.invert_first_k(head, 3)
        print "after:", L.to_array(head_new)

    # revert k - by - k
    if False:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new = L.invert_k_by_k(head, 4)
        print "after:", L.to_array(head_new)

    # merge sort
    if False:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new = L.merge_sort(head)
        print "after:", L.to_array(head_new)

    # delete k-th node from the end
    if True:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new, delete_node = L.delete_kth_from_end(head, 3)
        print "after:", L.to_array(head_new)
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

    def build_a_list_with_nodes(self, array):
        pivot = pre = Node(-1)
        nodes = []
        for val in array:
            cur = Node(val)
            pre.next = cur
            pre = pre.next
            nodes.append(cur)
        return pivot.next, nodes

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

    def get_intersection_node(self, headA, headB):
        p1 = headA
        p2 = headB
        while p1 != p2:
            if p1:
                p1 = p1.next
            else:
                p1 = headB
            if p2:
                p2 = p2.next
            else:
                p2 = headA
        return p1

    def merge_two_sorted_lists(self, l1, l2):
        pivot = Node(-1)
        pre = pivot
        p1 = l1
        p2 = l2
        while p1 and p2:
            if p1.val <= p2.val:
                pre.next = p1
                pre = pre.next
                p1 = p1.next
            else:
                pre.next = p2
                pre = pre.next
                p2 = p2.next
        while p1:
            pre.next = p1
            pre = pre.next
            p1 = p1.next
        while p2:
            pre.next = p2
            pre = pre.next
            p2 = p2.next
        return pivot.next

    def merge_k_sorted_lists(self, lists):
        # using a priority queue
        from Queue import PriorityQueue
        PQ = PriorityQueue()
        pivot = Node(-1)
        pre = pivot
        for l in lists:
            if l:
                PQ.put((l.val, l))
        while PQ.qsize():
            _, p = PQ.get()
            pre.next = p
            pre = pre.next
            p = p.next
            if p:
                PQ.put((p.val, p))
        return pivot.next

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
    if False:
        head = L.build_a_list(raw_list)
        print "before:", L.to_array(head)
        head_new, delete_node = L.delete_kth_from_end(head, 3)
        print "after:", L.to_array(head_new)

    # get intersection node
    if False:
        listA, listB = [], []
        for _ in range(10):
            listA.append(random.randint(0, 1000000))
            listB.append(random.randint(0, 1000000))
        headA, NodesA = L.build_a_list_with_nodes(listA)
        headB, NodesB = L.build_a_list_with_nodes(listB)
        # make intersection
        NodesB[5].next = NodesA[7]
        print "before, list A:", L.to_array(headA)
        print "before, list B:", L.to_array(headB)

        res = L.get_intersection_node(headA, headB)
        print "intersection node is:", res.val

    # merge two sorted list
    if False:
        l1 = [1,3,5,7,9]
        l2 = [2,4,6,8,10]
        h1 = L.build_a_list(l1)
        h2 = L.build_a_list(l2)
        print "before, list 1:", L.to_array(h1)
        print "before, list 2:", L.to_array(h2)
        l_new = L.merge_two_sorted_lists(h1, h2)
        print "after merge:", L.to_array(l_new)

    if True:
        ls = [
            [1,3,9,13,14],
            [2,6,8,10,16],
            [0,4,5,12],
            [7,11,15]
        ]
        lists = []
        for l in ls:
            h = L.build_a_list(l)
            lists.append(h)
        l_new = L.merge_k_sorted_lists(lists)
        print "after merge:", L.to_array(l_new)

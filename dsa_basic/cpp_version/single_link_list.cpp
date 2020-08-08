#include "single_link_list.h"

ListNode * SingleLinkList::build_a_list(std::vector<int> array) {
    ListNode * pre = new ListNode(-1);
    ListNode * p = pre;
    for (auto x : array) {
        ListNode * tmp = new ListNode(x);
        p->next = tmp;
        p = tmp;
    }
    return pre->next;
}

void SingleLinkList::display_a_list(ListNode * head) {
    ListNode * p = head;
    while (p) {
        std::cout << p->val;
        if (p->next) {
            std::cout << "->";
        }
        p = p->next;
    }
    std::cout << std::endl;
}

ListNode * SingleLinkList::revert(ListNode * head) {
    ListNode * pre = nullptr;
    ListNode * cur = head;
    while (cur) {
        ListNode * tmp = cur->next;
        cur->next = pre;
        pre = cur;
        cur = tmp;
    }
    return pre;
}

ListNode * SingleLinkList::delete_back_kth_node(ListNode * head, int k) {
    // delete the k-th node from tail to head
    ListNode *pre = new ListNode(-1);
    pre->next = head;
    ListNode *p1 = pre;
    ListNode *p2 = head;
    while (k--) {
        if (!p2) {
            return head;
        }
        p2 = p2->next;
    }
    while (p2) {
        p2 = p2->next;
        p1 = p1->next;
    }
    ListNode *tmp = p1->next;
    p1->next = p1->next->next;
    delete tmp;
    return pre->next;
}
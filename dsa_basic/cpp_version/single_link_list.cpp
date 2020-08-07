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
        std::cout << p->val << ",";
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
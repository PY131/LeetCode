#pragma once

#include<iostream>
#include <vector>
#include <string>

struct ListNode { 
    int val;
    ListNode * next;
    ListNode(int x) {
        val = x;
        next = nullptr;
    }
};

class SingleLinkList {

  public:
    ListNode * build_a_list(std::vector<int> array);
    void display_a_list(ListNode * head);
    ListNode * revert(ListNode * head);
};

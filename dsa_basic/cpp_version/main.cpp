#include <iostream>
#include "sorter.h"
#include "single_link_list.h"

using namespace std;

int main() {
    cout << "------------------mian() start------------------" << std::endl;

    // std::vector<int> raw_array = {1,3,5,7,9,2,4,6,8,10,9,3,1,5,7,2,5,8,3,1};
    // Sorter sorter;
    // sorter.show_array(raw_array, "before: ");
    // sorter.bubble_sort(raw_array);
    // sorter.quick_sort(raw_array);
    // sorter.merge_sort(raw_array);
    // sorter.heap_sort(raw_array);
    // sorter.show_array(raw_array, "after: ");

    std::vector<int> raw_array = {1,3,5,7,9,2,4,6,8,10};
    SingleLinkList L;
    ListNode * head = L.build_a_list(raw_array);
    L.display_a_list(head);
    ListNode * new_head = L.revert(head);
    L.display_a_list(new_head);
}
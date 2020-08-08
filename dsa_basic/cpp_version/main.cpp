#include <iostream>
#include <vector>
#include "sorter.h"
#include "single_link_list.h"
#include "binary_tree.h"
#include "dp.h"
#include "math.h"
#include "array_and_string.h"

void about_sort() {
    std::vector<int> raw_array = {1,3,5,7,9,2,4,6,8,10,9,3,1,5,7,2,5,8,3,1};
    Sorter sorter;
    // sorter.show_array(raw_array, "before: ");
    // sorter.bubble_sort(raw_array);
    // sorter.quick_sort(raw_array);
    // sorter.merge_sort(raw_array);
    // sorter.heap_sort(raw_array);
    // sorter.show_array(raw_array, "after: ");

    // std::string largest_num = sorter.largest_number(raw_array);
    // std::cout << largest_num << std::endl;
    
    std::vector<std::vector<int>> matrix = {{1,5,9}, {10,11,13}, {12,13,15}};
    int kth_smallest = sorter.kth_smallest(matrix, 8);
    std::cout << kth_smallest << std::endl;
}

void about_single_linked_list() {
    std::vector<int> raw_array = {1,3,5,7,9,2,4,6,8,10};
    SingleLinkList L;
    ListNode * head = L.build_a_list(raw_array);
    L.display_a_list(head);
    head = L.revert(head);
    head = L.delete_back_kth_node(head, 3);
    L.display_a_list(head);
}

void display_array(std::vector<int> &arr) {
    for (auto x: arr) {
        std::cout << x << ", ";
    }
    std::cout << std::endl;
}

void about_binary_tree() {
    std::vector<int> pres = {1,2,4,3,5,7,8,6};
    std::vector<int> ins = {4,2,1,7,5,8,3,6};
    BTree BT;
    TreeNode * root = BT.rebuild_a_tree(pres, ins);
    std::vector<int> traversal_res;

    traversal_res = BT.preorder(root);
    display_array(traversal_res);
    traversal_res = BT.preorder_iteratively(root);
    display_array(traversal_res);

    traversal_res = BT.inorder_iteratively(root);
    display_array(traversal_res);

    traversal_res = BT.postorder_iteratively(root);
    display_array(traversal_res);

    traversal_res = BT.level(root);
    display_array(traversal_res);

    traversal_res = BT.level_snake(root);
    display_array(traversal_res);
}

void about_dp() {
    DP dp;
    // std::cout << dp.fibonacci(3);
    // std::vector<int> array = {-2,1,-3,4,-1,2,1,-5,4};
    // std::cout << dp.max_sum_of_subarray(array);
    // std::vector<int> array = {10,9,2,5,3,7,101,18};
    // std::cout << dp.length_of_LIS(array);
}

void about_math() {
    Math M;
    std::vector<std::vector<int>> points = {{1,1}, {3,2}, {5,3}, {4,1}, {2,3}, {1,4}};
    std::cout << M.max_points(points) << std::endl;
}

void about_array_and_string() {
    ArrayString AS;
    // std::vector<int> nums = {2,7,11,15};
    // std::vector<int> res = AS.twoSum(nums, 9);
    // display_array(res);

    std::vector<int> nums1 = {1,3};
    std::vector<int> nums2 = {2};
    std::cout << findMedianSortedArrays(nums1, nums2) << std::endl;
}

int main() {
    std::cout << "------------------mian() start------------------" << std::endl;

    // about_sort();
    // about_single_linked_list();
    // about_binary_tree();
    // about_dp();
    // about_math();
    about_array_and_string();
}
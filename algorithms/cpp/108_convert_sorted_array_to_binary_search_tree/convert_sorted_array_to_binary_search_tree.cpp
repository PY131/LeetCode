//============================================================================
// Name        : 108_convert_sorted_array_to_binary_search_tree.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

#include "binary_tree.h"

/*********************************************************
 * Solution:
 *     consider using recursion.
 *     BST has the attribution like:
 *         1. Maximal: at the rightmost node;
 *         2. Minimal: at the far left node;
 *         3. Precursor: left child tree's rightmost;
 *         4. Successor: right child tree's far left;
 *
 **********************************************************/
class Solution {
public:
    TreeNode* sortedArrayToBST(vector<int>& nums) {
        if(nums.size() == 0) return NULL;
//        if(nums.size() == 1){
//            return new TreeNode(nums[0]);
//        }
        int middle = nums.size()/2;
        TreeNode *root = new TreeNode(nums[middle]);

        vector<int> left_nums(nums.begin(), nums.begin() + middle);
        vector<int> right_nums(nums.begin() + middle + 1, nums.end());
        root->left = sortedArrayToBST(left_nums);
        root->right = sortedArrayToBST(right_nums);

        return root;
    }
};

int main() {
    int data[] = {3,9,20,22,25};
    vector<int> nums(data, data + 5);
    TreeNode *root = NULL;

    Solution s;
    root = s.sortedArrayToBST(nums);

    clearBTree(root);
    return 0;
}

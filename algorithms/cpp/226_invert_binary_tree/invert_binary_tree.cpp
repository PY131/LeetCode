//============================================================================
// Name        : 226_invert_binary_tree.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

//#include "binary_tree.h"

/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode(int x) : val(x), left(NULL), right(NULL) {}
 * };
 */

class Solution {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root != NULL){
            // here we can just use swap and recursion
            swap(root -> left, root -> right);
            invertTree(root -> left);
            invertTree(root -> right);
        }
        return root;
    }
};

class Solution2 {
public:
    TreeNode* invertTree(TreeNode* root) {
        if(root != NULL){
            TreeNode *temp = root -> left;
            root -> left = root -> right;
            root -> right = temp;
            invertTree(root -> left);
            invertTree(root -> right);
        }
        return root;
    }
};

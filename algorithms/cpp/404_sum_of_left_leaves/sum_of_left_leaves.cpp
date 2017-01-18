//============================================================================
// Name        : 404_sum_of_left_leaves.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#include "binary_tree.h"

/************************************************************
 * class name: Solution
 * function: calculating the sum of all left leaves node in a binary tree.
 * idea: using recursive for sum
 * synopsis:
 *   recursing assumption:
 *     parameter isn's a leaf node
 *   if:
 *     a node's child node also isn't leaf node, just recursion.
 *   else:
 *     a node's left child node is a left leaf, add the value.
 *************************************************************/
class Solution {
public:
    int sumOfLeftLeaves(TreeNode* root) {
    	int sum = 0;

    	//1. judge Non empty
    	if(root == NULL) return 0;
    	//2.judge whether the node's left child is a leaf node
    	if(root->left != NULL && root->left->left == NULL && root->left->right == NULL)
    		sum += root->left->val;
    	//3.recursion continue
		sum += sumOfLeftLeaves(root->left);  //no need of non-empty checking cause of step 1.
		sum += sumOfLeftLeaves(root->right);

    	return sum;
    }
};

int main() {
	int data[] = {3,9,20,NULL,NULL,15,7};
	TreeNode *root = NULL;
	Solution s;

	root = creatBTree(data, 0, 7);
	cout<< "the sum is: " << s.sumOfLeftLeaves(root) << endl;
	clearBTree(root);

	return 0;
}

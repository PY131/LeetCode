/*
 * binary_tree.h
 *
 *  Created on: 2017Äê1ÔÂ17ÈÕ
 *      Author: PY131
 */

/*
 * refer to:
 * 	http://blog.csdn.net/haoyuedangkong_fei/article/details/51840963
 */

#ifndef BINARY_TREE_H_
#define BINARY_TREE_H_

#include <iostream>
using namespace std;

//Definition for a binary tree node.
struct TreeNode {
	int val;
	TreeNode *left;
	TreeNode *right;
	TreeNode(int x) : val(x), left(NULL), right(NULL) {}  //constructor
};

TreeNode * creatBTree(int data[], int index, int n);  //creating binary tree using array[]
void clearBTree(TreeNode *treeNode);  //clear a binary tree

#endif /* BINARY_TREE_H_ */

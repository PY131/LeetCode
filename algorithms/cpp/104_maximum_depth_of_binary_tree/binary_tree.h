/*
 * binary_tree.h
 *
 *  Created on: 2017Äê1ÔÂ13ÈÕ
 */

#ifndef BINARY_TREE_H_
#define BINARY_TREE_H_

#include <iostream>
using namespace std;

// Definition for a binary tree node.
struct TreeNode {
    int val;
    TreeNode *left;
    TreeNode *right;
    TreeNode(int x) : val(x), left(NULL), right(NULL) {}
};

TreeNode * InitTree();  //initial a binary tree(BT)

TreeNode *TreeFindNode(TreeNode *treeNode, int value); //search a node

void AddTreeNode(TreeNode *treeNode);  //add leaf node to BT

void ClearTree(TreeNode *treeNode);  //delete a BT

#endif /* BINARY_TREE_H_ */

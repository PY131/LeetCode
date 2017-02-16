/*
 * binary.tree.cpp
 *
 *  Created on: 2017年1月17日
 *      Author: PY131
 */

#include "binary_tree.h"

/*
 * using data[] array to creating binary tree
 * parameter:
 * 	data: number array for binary tree
 * 	index: root layer counting
 * 	n: total nodes number
 */
TreeNode * creatBTree(int data[], int index, int n)
{
	TreeNode * pNode = NULL;

	if(index < n && data[index] != NULL)  //数组中NULL表示该节点为空
	{
		pNode = (TreeNode *)malloc(sizeof(TreeNode));  //alloc mem space
		if(pNode == NULL)
			return NULL;
		pNode->val = data[index];
		pNode->left = creatBTree(data, 2 * index + 1, n);  //loop through the b_tree using layer index, form 0 on
		pNode->right = creatBTree(data, 2 * index + 2, n);
	}

	return pNode;
}

/*
 * delete a tree
 */
void clearBTree(TreeNode *treeNode)
{
	if(treeNode != NULL)  //check whether
	{
		clearBTree(treeNode->left);
		clearBTree(treeNode->right);
		delete treeNode;
	}
}

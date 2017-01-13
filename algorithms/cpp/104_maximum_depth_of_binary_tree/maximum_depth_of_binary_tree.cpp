//============================================================================
// Name        : 104_maximum_depth_of_binary_tree.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#include "binary_tree.h"

class Solution {
public:
	int maxDepth(TreeNode* root) {
		if(root == NULL) return 0;
		else return 1 + max( maxDepth(root->left), maxDepth(root->right));
	}
};

int main() {
	Solution s1;
	TreeNode *root = InitTree();

	AddTreeNode(root);  //just a example
	AddTreeNode(root);
	AddTreeNode(root);

	cout << s1.maxDepth(root) << endl;
	ClearTree(root);

	return 0;
}





//============================================================================
// Name        : 100_same_tree.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

# include "binary_tree.h"

/****************************************************
 * here is the basic method using recursive
 *****************************************************/
class Solution {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
    	if( p == NULL && q == NULL )  return true;
    	else{
    		if( p != NULL && q != NULL && p->val == q->val )
        		return isSameTree(p->left, q->left) && isSameTree(p->right, q->right);
        	else return false;
    	}
    }
};

/****************************************************
 * this is more concise than Solution
 *****************************************************/
class Solution1 {
public:
    bool isSameTree(TreeNode* p, TreeNode* q) {
    	if( p == NULL || q == NULL )  return (p == q);
    	else return ( p->val == q->val && isSameTree(p->left, q->left) && isSameTree(p->right, q->right) );
    }
};

int main() {
	int data1[] = {3,9,20,NULL,NULL,1,7};
	int data2[] = {3,9,20,NULL,NULL,15,7};
	TreeNode *p = NULL;
	TreeNode *q = NULL;
	p = creatBTree(data1, 0, 7);
	q = creatBTree(data2, 0, 7);

	Solution1 s;
	cout<< "output: " << s.isSameTree(p, q) << endl;
	clearBTree(p);
	clearBTree(q);

	return 0;
}

/*
 * binary_tree.cpp
 *
 *  Created on: 2017Äê1ÔÂ13ÈÕ
 */

#include <iostream>
using namespace std;

#include "binary_tree.h"

/*
 * initial a tree with it's root node
 */
TreeNode * InitTree()
{
	TreeNode * node;
	int x = 0;
	if((node = new TreeNode(x)) != NULL){
		cout << "input root node value" << endl;
		cin >> x;
		node->val = x;
		if(node != NULL){
			return node;
		}
		else{
			return NULL;
		}
	}
	return NULL;
}

/*
 * searching a node with it's value
 * parameters:
 * 		treeNode: starting node
 * 		value: target node value
 * return:
 * 		target node pointer
 */
TreeNode *TreeFindNode(TreeNode *treeNode, int value)
{
	TreeNode *ptr;
	if(treeNode == NULL){
		return NULL;
	}
	else{
		if(treeNode -> val == value){
			return treeNode;
		}
		else{  //searching from left to right (child tree)
			if((ptr = TreeFindNode(treeNode -> left, value)) != NULL){  //left searching recursively
				return ptr;
			}
			else if(( ptr = TreeFindNode(treeNode -> right, value)) != NULL){  //right searching recursively
				return ptr;
			}
			else
			{
				return NULL;
			}
		}
	}
}

/*
 * adding a node
 * parameters:
 * 		treeNode: adding node's parent
 */
void AddTreeNode(TreeNode *treeNode)
{
	TreeNode *pnode,*parent;
	int x = 0;
	char menusel;  //for keyboard input opinion

	if((pnode = new TreeNode(x)) != NULL){     //allocation memory space
		cout << "input target node value£º" << endl;  //initial this leaf node
		cin >> x;
		pnode->val = x;

		cout << "input target parent value: " << endl;
		cin >> x;
		parent = TreeFindNode(treeNode, x);  //get the parent pointer

		if(parent == NULL){
			cout<<"no such a parent"<<endl;
			delete pnode;
			return ;
		}

		cout<<"select: 1 : add into left£»2 : add into right"<<endl;
		do{
			cin >> menusel;
			if(menusel == '1' || menusel == '2'){
				switch(menusel){
					case '1':     //add to left child
						if(parent->left){    //check whether add able
							cout<<"can not add"<<endl;
						}
						else{
							parent -> left = pnode;
							cout<<"add success!"<<endl;
						}
						break;
					case '2':     //add to left child
						if(parent->right){   //check whether add able
							cout<<"can not add"<<endl;
						}
						else
						{
							parent -> right = pnode;
							cout<<"add success!"<<endl;
						}
						break;
					default:
						cout<<"input error!"<<endl;
						break;
				}
			}
		}while(menusel != '1' && menusel != '2');
	}
}

/*
 * delete a tree
 */
void ClearTree(TreeNode *treeNode)
{
	if(treeNode != NULL)  //check whether
	{
		ClearTree(treeNode->left);
		ClearTree(treeNode->right);
		delete treeNode;
	}
}







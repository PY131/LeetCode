//============================================================================
// Name        : 237_delete_node_in_a_linked_list.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;
#include "linked_list.h"

/*
 * assumption: the node isn's the end one
 */
class Solution {
public:
    void deleteNode(ListNode* node) {
    	//1st: consider assign next node to this one
    	ListNode * temp = node->next;
    	node->val = node->next->val;
    	node->next = node->next->next;
    	//2nd: delete the next node
    	delete temp;
    }
};

int main() {
	int data[] = {1,2,3,4};
	int i, n = 4;
	ListNode * node = NULL;
	ListNode * Head = createList(data, 0, n);
	Solution s;

	cout << "the raw list is: ";
	node = Head;
	for(i = 0; i < n; i++){
		cout << node->val << " ";
		node = node->next;
	}
	cout << endl;

	s.deleteNode(Head->next->next);  //delete 3rd node

	cout << "the new list is: ";
	node = Head;
	for(i = 0; i < n - 1; i++){
		cout << node->val << " ";
		node = node->next;
	}
	cout << endl;

	return 0;
}

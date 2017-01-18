/*
 * linked_list.cpp
 *
 *  Created on: 2017Äê1ÔÂ18ÈÕ
 *      Author: Peng
 */

#include "linked_list.h"

/*
 * create a list based on an array<int>
 * parameter:
 *     data:
 *       array mapping the singly linked list.
 *     index:
 *       the starting index in the recursive. (set to 0 on for the first recursion)
 *     n:
 *       the number of list's nodes.
 */
ListNode *createList(int data[], int index, int n){
	ListNode *head = NULL;

	if(index < n)  //the max index is n
	{
		head = (ListNode *)malloc(sizeof(ListNode));
		if(head == NULL)
			return NULL;
		head->val = data[index];
		head->next = createList(data, index + 1, n);  //loop through the b_tree using index, from 0 on
	}
	return head;
}

/*
 * clear a list
 */
void clearList(ListNode *Head){
	if(Head != NULL)  //check whether
	{
		clearList(Head->next);
		delete Head;
	}
}


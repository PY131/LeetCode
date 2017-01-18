/*
 * linked_list.h
 *
 *  Created on: 2017Äê1ÔÂ18ÈÕ
 *      Author: 
 */

#ifndef LINKED_LIST_H_
#define LINKED_LIST_H_
#include <iostream>

/*
 * refer to:
 *     http://www.cnblogs.com/cyttina/archive/2012/10/25/2740372.html
 */

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

ListNode *createList(int data[], int index, int n);  //create a list
void clearList(ListNode *Head);  //clear a list

#endif /* LINKED_LIST_H_ */

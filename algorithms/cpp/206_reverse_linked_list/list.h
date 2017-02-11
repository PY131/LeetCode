/*
 * list.h
 *
 *  Created on: 2017��2��11��
 *      Author: Peng
 */

#ifndef LIST_H_
#define LIST_H_

#include <iostream>

// Definition for singly-linked list.
struct ListNode {
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
//    ListNode(int x, ListNode* ptr = 0) : val(x), next(ptr){}
};

class IntSLList
{
public:
    IntSLList();
    ~IntSLList();

    bool IsEmpty();
    void AddToHead(int el);
    void AddToTail(int el);
    void DeleteFromHead();
    void DeleteFromTail();
    void DeleteNode(int el);
    bool IsInList(int el);

    void ReverseList(); //��ת����

    ListNode* GetListHead();  //��ȡ����ͷ�ڵ�

private:
    ListNode* head;
    ListNode* tail;
};

#endif /* LIST_H_ */

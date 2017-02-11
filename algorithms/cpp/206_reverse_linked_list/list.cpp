/*
 * list.cpp
 *
 *  Created on: 2017Äê2ÔÂ11ÈÕ
 *      Author: Peng
 */


#include "list.h"
#include <iostream>
using namespace std;

IntSLList::IntSLList()
{
    head = tail = NULL;
}

IntSLList::~IntSLList()
{

}

bool IntSLList::IsEmpty()
{
    return head == NULL;
}

void IntSLList::AddToHead(int el)
{
    head = tail = new ListNode(el);
    if (tail == 0)
    {
        tail = head;
    }
}

void IntSLList::AddToTail(int el)
{
    if (tail == NULL)
    {
        head = tail = new ListNode(el);
    }
    else
    {
        tail->next = new ListNode(el);
        tail = tail->next;
    }
}

void IntSLList::DeleteFromHead()
{
    if (head != NULL)
    {
        ListNode* ptemp = head;
        head = head->next;
        delete ptemp;
        ptemp = NULL;
    }
}

void IntSLList::DeleteFromTail()
{
    if (tail != NULL)
    {
        if (head == tail)
        {
            delete tail;
            head = tail = NULL;
        }
        else
        {
            ListNode* ptemp = head;
            while (ptemp->next != tail)
            {
                ptemp = ptemp->next;
            }

            delete tail;
            tail = ptemp;
            tail->next = NULL;
        }
    }
}

void IntSLList::DeleteNode(int el)
{
    if (head != NULL)
    {
        if (head == tail && head->val == el)
        {
            delete head;
            head = tail = NULL;
        }
        else if (head->val == el)
        {
            ListNode* ptemp = head;
            head = head->next;
            delete ptemp;
            ptemp = NULL;
        }
        else if (head->next != NULL)
        {
            ListNode* pFront = head;
            ListNode* pBehind = head->next;
            while (pBehind != 0)
            {
                if (pBehind->val == el)
                {
                    pFront->next = pBehind->next;
                    if (pBehind == tail)
                        tail = pFront;

                    delete pBehind;
                    pBehind = NULL;
                    break;
                }

                pFront = pBehind;
                pBehind = pBehind->next;
            }
        }
    }
}

bool IntSLList::IsInList(int el)
{
    ListNode* ptemp = head;
    while (ptemp != NULL)
    {
        if (ptemp->val == el)
            return true;

        ptemp = ptemp->next;
    }

    return false;
}

void IntSLList::ReverseList()
{
    if (head != tail)
    {
        ListNode* p1 = head;
        ListNode* p2 = head->next;
        ListNode* p3 = NULL;
        p1->next = NULL;
        while (p2 != NULL)
        {
            p3 = p2->next;
            p2->next = p1;
            p1 = p2;
            p2 = p3;
        }

        swap(head, tail);
    }
}

ListNode* IntSLList::GetListHead()
{
    return head;
}



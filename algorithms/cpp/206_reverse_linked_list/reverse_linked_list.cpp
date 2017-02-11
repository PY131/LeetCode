//============================================================================
// Name        : 206_reverse_linked_list.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#include "list.h"

/*********************************************************************
 * Solution 1:
 *     here we considering the recursive method;
 **********************************************************************/
class Solution1 {
public:
    ListNode* reverseList(ListNode* head) {
        if(head == NULL || head->next == NULL) return head;  //if empty or single node
        else{
            ListNode *new_head = reverseList(head->next); //recursive
            head->next->next = head;
            head->next = NULL; //reversing
            return new_head;
        }
    }
};

// printing a list
void Print(ListNode* head)
{
    while (head != NULL)
    {
        cout << head->val << " ";
        head = head->next;
    }
    cout << endl;
}

int main()
{
    IntSLList raw_list;
    for(int i = 0; i < 6; i++){
        raw_list.AddToTail(i);
    }
    ListNode* raw_head = raw_list.GetListHead();
    Print(raw_head);  //print the list

    //1st: using existed method for reversing
    raw_list.ReverseList();
    raw_head = raw_list.GetListHead();
    Print(raw_head);

    //2nd: using Solution 1
    Solution1 s1;
    Print(s1.reverseList(raw_head));

    return 0;
}

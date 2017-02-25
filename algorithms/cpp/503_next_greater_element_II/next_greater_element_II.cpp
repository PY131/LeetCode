//============================================================================
// Name        : 503_next_greater_element_II.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <stack>  //for solution 2
using namespace std;

/*************************************************************************
 * Solution 1:
 *      using traversal directly.
 *************************************************************************/
class Solution1 {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        vector<int> res;

        for(vector<int>::size_type i = 0; i < nums.size(); i++){
            for(vector<int>::size_type j = i+1; ; j++){
                if(j == nums.size()) j = 0;
                if(j == i){
                    res.push_back(-1);
                    break;
                }
                if(nums[i] < nums[j]){
                    res.push_back(nums[j]);
                    break;
                }
            }
        }

        return res;
    }
};

/*************************************************************************
 * Solution 2:
 *   Principle:
 *      Suppose we have a decreasing sequence followed by a greater number's index
 *      For example [5, 4, 3, 2, 1, 6]
 *      then the greater number 6 is the next greater element for all previous numbers.
 *   Method:
 *      here using "stack" to get the next greater number and pop to update all the previous.
 *
 *************************************************************************/
class Solution2 {
public:
    vector<int> nextGreaterElements(vector<int>& nums) {
        int n = nums.size();

        vector<int> res(n, -1);
        stack<int> s;

        for(int i = 0; i < 2*n; i++){
            int num = nums[i % n];
            while (!s.empty() && nums[s.top()] < num) {  //next greater appears and update all the previous
                res[s.top()] = num;  //updating the previous
                s.pop();  //pop the updated one
            }
            if (i < n) s.push(i);
        }

        return res;
    }
};

/*********************************************
 * Function:
 *     printing vector
 *********************************************/
template<class T>
void print_vec(vector<T>& res){
    for(auto it : res){
        cout << it <<" "; // prints
    }
    cout << endl;
    return;
}

int main() {
    vector<int> nums {5,4,3,2,1};

    Solution1 s1;
    vector<int> res = s1.nextGreaterElements(nums);
    print_vec(res);

    Solution2 s2;
    res = s2.nextGreaterElements(nums);
    print_vec(res);

    return 0;
}

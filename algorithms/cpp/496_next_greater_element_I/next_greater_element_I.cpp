//============================================================================
// Name        : 496_next_greater_element_I.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <unordered_map>  //for solution 2 & 3
#include <stack>  //for solution 3
using namespace std;

/*************************************************************************
 * Solution 1:
 *      using traversal directly.
 *************************************************************************/
class Solution1 {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> res;

        for(int num1 : findNums){
            for(vector<int>::size_type i = 0; i < nums.size(); i++){
                if(nums[i] == num1){
                    vector<int>::size_type j = i+1;
                    for(; j < nums.size(); j++){
                        if(nums[j] >= num1){
                            res.push_back(nums[j]);
                            break;
                        }
                    }
                    if(j == nums.size())  res.push_back(-1);
                }
            }
        }

        return res;
    }
};

/*************************************************************************
 * Solution 2:
 *      using "hash_map" to mapping the equal numbers between two arrays.
 *************************************************************************/
class Solution2 {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> res;

        unordered_map<int, int> m;
        for(vector<int>::size_type i = 0; i < nums.size(); i++){
            m[nums[i]] = i;
        }
        for(int num1 : findNums){
            vector<int>::size_type j = m[num1] + 1;
            for(; j < nums.size(); j++){
                if(nums[j] > num1){
                    res.push_back(nums[j]);
                    break;
                }
            }
            if(j == nums.size())  res.push_back(-1);
        }

        return res;
    }
};


/*************************************************************************
 * Solution 3:
 *      using "hash_map" to mapping the numbers with it next greater number.
 *      here using "stack" to get the next greater number value.
 *************************************************************************/
class Solution3 {
public:
    vector<int> nextGreaterElement(vector<int>& findNums, vector<int>& nums) {
        vector<int> res;

        unordered_map<int, int> m;
        stack<int> s;

        for(int num2 : nums){
            while(!s.empty() && num2 > s.top()){  //next greater appears
                m[s.top()] = num2;  //set mapping
                s.pop();  //pop the old one
            }
            s.push(num2);  //update the new one
        }
        for(int num1 : findNums){
            res.push_back( m.count(num1) ? m[num1] : -1 );  //1 if an element with a key equivalent to k is found, or zero otherwise.
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
    vector<int> findnums {4,1,2};
    vector<int> nums {1,3,4,2};

    Solution1 s1;
    vector<int> res = s1.nextGreaterElement(findnums, nums);
    print_vec(res);

    Solution2 s2;
    res = s2.nextGreaterElement(findnums, nums);
    print_vec(res);

    Solution3 s3;
    res = s3.nextGreaterElement(findnums, nums);
    print_vec(res);

    return 0;
}

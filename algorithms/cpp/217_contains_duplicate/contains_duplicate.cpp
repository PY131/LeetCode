//============================================================================
// Name        : 217_contains_duplicate.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>  //for Solution 1
#include <unordered_set>  //for Solution 2 & 3
using namespace std;

/**************************************************************
 * Solution 1:
 *     using sorting and compare the neighbors
 * Time complexity:
 *     depending on sort(), default O(NlgN)
 ***************************************************************/
class Solution1 {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.empty()) return false;
        sort(nums.begin(), nums.end());  //O(NlgN)

        for(vector<int>::size_type i = 0; i < nums.size() - 1; i++){  //O(N)
            if(nums[i] == nums[i+1]) return true;
    	}
        return false;
    }
};

/**************************************************************
 * Solution 2:
 *     using hash set (unordered_set) and size comparing.
 * Time complexity & Space complexity:
 *     O(N)    O(N)
 ***************************************************************/
class Solution2 {
public:
    bool containsDuplicate(vector<int>& nums) {
        unordered_set<int> nums_set(nums.begin(), nums.end());

        if(nums.size() != nums_set.size()) return true;
        else return false;
    }
};

/**************************************************************
 * Solution 3:
 *     also use hash set (unordered_set) but just checking the repeat.
 * Time complexity & Space complexity:
 *     O(N)    <O(N)
 ***************************************************************/
class Solution3 {
public:
    bool containsDuplicate(vector<int>& nums) {
        if(nums.empty()) return false;
        unordered_set<int> nums_set;

        for(vector<int>::size_type i = 0; i < nums.size(); i++){  //O(N)
            if(nums_set.find(nums[i]) != nums_set.end()) return true;
            else nums_set.insert(nums[i]);
        }
        return false;
    }
};

int main() {
    int a[8] = {3,3};
    vector<int> nums(a, a+2);

    Solution1 s1;
    Solution2 s2;
    Solution3 s3;
    cout << s1.containsDuplicate(nums) << endl; // prints
    cout << s2.containsDuplicate(nums) << endl; // prints
    cout << s3.containsDuplicate(nums) << endl; // prints

    return 0;
}

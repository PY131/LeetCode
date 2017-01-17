//============================================================================
// Name        : 349_intersection_of_two_arrays.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <iterator>  //for printing
#include <vector>  //for vector
#include <unordered_set>  //for unordered_set
using namespace std;

/*
 * using <unordered_set> LIB to eliminate repeat number.
 * fun1:
 * 		count(): check whether exists in the vector
 *		erase(): remove the checked items
 */
class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<int> ins;
        unordered_set<int> s(nums1.begin(), nums1.end());  //build a unordered set

        for(int num : nums2){
            if(s.count(num) != 0){  //the number exists in unordered nums1
                ins.push_back(num);
                s.erase(num);  //remove checked number
            }
        }

        return ins;
    }
};

int main() {
	vector<int> nums1 = {1, 1, 2, 4, 4, 5, 12};
	vector<int> nums2 = {4, 4, 5, 6, 7, 8, 12};
	vector<int> ins;

	Solution s;
	ins = s.intersection(nums1, nums2);

	copy(ins.begin(), ins.end(), ostream_iterator<int> (cout, "\n"));

	return 0;
}

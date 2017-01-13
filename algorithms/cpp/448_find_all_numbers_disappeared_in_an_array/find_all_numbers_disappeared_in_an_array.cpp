//============================================================================
// Name        : 448_find_all_numbers_disappeared_in_an_array.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <iterator>
using namespace std;

class Solution {
public:
    vector<int> findDisappearedNumbers(vector<int>& nums) {
    	int i, j, len = nums.size();
    	vector<int> nums_loss;

    	for(i = 0; i < len; i++){
        	j = abs(nums[i]) - 1;
        	if(nums[j] > 0)  nums[j] = -nums[j];
       }
    	for(i = 0; i < len; i++){
    		if(nums[i] > 0)  nums_loss.push_back(i+1);
    	}
    	return nums_loss;
    }
};

int main() {
	Solution s1;
	vector<int> nums1;
	int  v[10] = {5,2,2,2,3,3,1,1,9,10};

	nums1.reserve(10);
	nums1.insert(nums1.begin(), &v[0], &v[9]);
	nums1 = s1.findDisappearedNumbers(nums1);

	cout << "the disapperared numbers are:"<< endl;
	copy(nums1.begin(), nums1.end(), ostream_iterator<int> (cout, " "));
}

//============================================================================
// Name        : 136_single_number.cpp
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
    int singleNumber(vector<int>& nums) {
    	/*
    	 * consider the associative property of XOR
    	 * example: a^b^c = a^(b^c)
    	 */
    	for(vector<int>::size_type i = 1; i < nums.size(); i++){
			nums[0] ^= nums[i];
		}
		return nums[0];
    }
};

int main() {
	Solution s1;	//preparing data
	int number;
	int v[7] = {1,2,2,1,5,3,5};
	vector<int> nums1;
	nums1.reserve(7);
	nums1.assign(&v[0],&v[7]);

	number = s1.singleNumber(nums1);	//executing

	copy(nums1.begin(), nums1.end(), ostream_iterator<int> (cout, " "));	//printing
	cout << "the single number is:"<< number << endl;

	return 0;
}

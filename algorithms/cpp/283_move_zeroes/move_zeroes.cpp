//============================================================================
// Name        : 283_move_zeroes.cpp
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
    void moveZeroes(vector<int>& nums) {
    	vector<int>::size_type i, j;

    	/*
    	 * consider swap between zero and non-zero;
    	 * as well as right shift for vector index to ensure the sequence
    	 */
    	for(i = 0, j = 0; i < nums.size(); i++){
    		if(nums[i] != 0){
    			swap(nums[i], nums[j]);
    			j++;
    		}
    	}
    }
};

int main() {
	Solution s;

//	int iarray[] = {1, 0, 0, 2, 3, 0, 4};
//	size_t count = sizeof(iarray)/sizeof(int);
//	vector<int> num(iarray,iarray+count);

	vector<int> num = {1, 0, 0, 2, 3, 0, 4};  //C++11 supporting

	s.moveZeroes(num);
	copy(num.begin(), num.end(), ostream_iterator<int> (cout, "\n"));  //printing

	return 0;
}

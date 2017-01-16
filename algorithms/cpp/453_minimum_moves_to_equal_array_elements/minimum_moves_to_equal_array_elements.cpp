//============================================================================
// Name        : 453_minimum_moves_to_equal_array_elements.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
//#include <numeric>
#include <algorithm>
using namespace std;

class Solution {
public:
    int minMoves(vector<int>& nums) {
    	int k;
    	/*
    	 * 1_st: we set some variables:
    	 *     k:
    	 *         the moves (target variable)
    	 *     a_min:
    	 *         original array's minimum number {a1, a2, ... an}
    	 *     A:
    	 *         the final array value (all equal)
    	 *     sum:
    	 *         the sum of original array
    	 *     delta_sum:
    	 *         the sum of array when moving
    	 *
    	 * 2_nd: we give out the analysis:
    	 *     2.1.1.the sum of original array:
    	 *         sum = a1 + a2 + ... +an
    	 *     2.1.2.the change sum:
    	 *         delta_sum = k * (n-1)
    	 *     2.1.3.moves limitation:
    	 *         A <= k + a_min (less or equal)
    	 *
    	 *     2.2 so we can have:
    	 *         A * n = sum + delta_sum
    	 *    -->  A * n = sum + k * (n-1)
    	 *    -->  (k + a_min) * n >= sum + k * (n-1)
    	 *    -->  k >= sum - n * a_min
    	 *
    	 * for example: array = [1, 2, 3]
    	 *         sum = 6; a_min * n = 3;
    	 *     st. k >= 6 - 3 = 3;
    	 *     st. k(min) = 3;
    	 */
    	int sum = 0, a_min;
    	vector<int>::size_type i;
    	for(i = 0; i < nums.size(); i++)
    	{
    		sum += nums[i];  //calculating the sum of original array
    	                     // here can also use accumulate() in <numeric>
    	}
    	a_min = *min_element(nums.begin(), nums.end());  //calculating the min
    	k = sum - a_min * nums.size();

    	return k;
    }
};

int main() {
	Solution s;
	vector<int> num = {2,3,1,4};

	cout << s.minMoves(num) << endl; // prints
	return 0;
}

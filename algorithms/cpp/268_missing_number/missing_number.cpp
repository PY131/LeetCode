//============================================================================
// Name        : 268_missing_number.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

/***************************************************************
 * Solution 1:
 *     assume that missing one is x.
 *     st: the completed array is: nums U {x}, whose sum is n*(n-1)/2, (n = lenght)
 *     st: x = sum_of(nums U {x}) - sum_of(nums).
 * Complexity:
 *     time: O(N);
 *     space: 1;
 ****************************************************************/
class Solution1 {
public:
    int missingNumber(vector<int>& nums) {
        int n = nums.size();
        int sum = 0;
        for(int i = 0; i < n; i++){
            sum += nums[i];
        }
        return (n)*(n+1)/2 - sum;
    }
};

/***************************************************************
 * Solution 2:
 *     we can check sequential
 *     to see whose index isn't equaling to the value
 * Complexity:
 *     time: O(N*lgN);
 *     space: 1;
 ****************************************************************/
class Solution2 {
public:
    int missingNumber(vector<int>& nums) {
        int i;
        sort(nums.begin(), nums.end());
        for(i = 0; i < nums.size(); i++){
            if(i != nums[i]) return i;
        }
        return -1;
    }
};


/***************************************************************
 * Solution 3: expand from Solution 2
 *     considering in a completed array,
 *     a number's index always equal to a number's value,
 *     but now, except the missing one;
 *     which reminds me of XOR operator.
 * Complexity:
 *     time: O(N);
 *     space: 1;
 ****************************************************************/
class Solution3 {
public:
    int missingNumber(vector<int>& nums) {
        int res = nums.size();
        for(int i = 0; i < nums.size(); i++){
            res ^= i;
            res ^= nums[i];
        }
        return res;
    }
};

int main() {
    int a[5] = {0,1,2,4,5};
    vector<int> nums(a, a+5);

    Solution1 s1;
    Solution2 s2;
    Solution3 s3;
    cout << s1.missingNumber(nums) << endl;
    cout << s2.missingNumber(nums) << endl;
    cout << s3.missingNumber(nums) << endl;

    return 0;
}

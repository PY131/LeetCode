//============================================================================
// Name        : 121_best_time_to_buy_and_sell_stock.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

/******************************************************************
 * Solution 1:
 *     comparing by sequential;
 * Complexity:
 *     time:  O(N)
 *******************************************************************/
class Solution1 {
public:
    int maxProfit(vector<int>& prices) {
        if(prices.empty())  return 0;

        int dif = 0;
        int dif_temp = 0;
        int min_temp = prices[0];

        for(vector<int>::size_type i = 1; i < prices.size(); i++){
            if(prices[i] < min_temp){
                min_temp = prices[i];
                dif = dif_temp;
            }
            else if((prices[i] - min_temp) > dif_temp)
                dif_temp = prices[i] - min_temp;
        }
        if(dif < dif_temp) dif = dif_temp;

        return dif;
    }
};

/******************************************************************
 * Solution 2:
 *     comparing by sequential, more short and clear than solution 1;
 * Complexity:
 *     time:O(N)
 *******************************************************************/
class Solution2 {
public:
    int maxProfit(vector<int>& prices) {
        int maxPro = 0;
        int minPrice = INT_MAX;

        for(vector<int>::size_type i = 0; i < prices.size(); i++){
            minPrice = min(minPrice, prices[i]);  //find the min_temp;
            maxPro = max(maxPro, prices[i] - minPrice);  //find the dif_temp;
        }

        return maxPro;
    }
};

/******************************************************************
 * Solution 3:
 *     considering using Kadane's Algorithm in Maximum subarray problem;
 * Complexity:
 *     time:O(N)
 *******************************************************************/
class Solution3 {
public:
    int maxProfit(vector<int>& prices) {  //1st: calculating the difference of contiguous subarray
        if(prices.size() < 2) return 0;

        vector<int>  diff;  //storing the difference
        for(vector<int>::size_type i = 1; i < prices.size(); i++){
            diff.push_back(prices[i] - prices[i-1]);
        }
        return maxSubArray(diff);
    }

    int maxSubArray(vector<int>& nums) {  //2nd: using Kadane's Algorithm
        if(nums.size() < 1) return 0;

        int preMax = 0, m = 0;
        for(vector<int>::size_type i = 0; i < nums.size(); i++){
            m = max(m, preMax + nums[i]);
            preMax = max(0, preMax + nums[i]);
        }
        return m;
    }
};

int main() {
    int a[3] = {2,4,1};
    vector<int> prices(a, a + 3);

    Solution1 s1;
    cout << s1.maxProfit(prices) << endl; // prints
    Solution1 s2;
    cout << s2.maxProfit(prices) << endl; // prints
    Solution1 s3;
    cout << s3.maxProfit(prices) << endl; // prints

    return 0;
}

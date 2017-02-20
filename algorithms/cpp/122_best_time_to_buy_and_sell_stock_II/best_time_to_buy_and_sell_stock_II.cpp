//============================================================================
// Name        : 122_best_time_to_buy_and_sell_stock_II.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

/**********************************************************************
 * just calculating the sum of positive difference during two days;
 *********************************************************************/
class Solution1 {
public:
    int maxProfit(vector<int>& prices) {
        int res = 0;
        for (vector<int>::size_type i = 1; i < prices.size(); i++)
            res += max(prices[i] - prices[i-1], 0);
        return res;
    }
};

int main() {
    int a[6] = {2,4,1,3,2,6};
    vector<int> prices(a, a + 6);

    Solution1 s1;
    cout << s1.maxProfit(prices) << endl; // prints

    return 0;
}

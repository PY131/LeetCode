//============================================================================
// Name        : 309_best_time_to_buy_and_sell_stock_with_cooldown.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

/**************************************************************
 * Solution 1:
 *     it seems to be a DP problems;
 *     so we define the states first and then conduct the transition function
 *     1.states:
 *          buy[i]:
 *              means the maxProfit after day i with the state of buy (own 1 stock);
 *          sell[i]:
 *              means the maxProfit after day i with the state of sell (own 0 stock);
 *          rest[i]:
 *              means the maxProfit after day i with the state of rest (do nothing);
 *     2.transition function:
 *          2.1.constraint conditions:
 *              sell after buy, buy after rest;
 *          2.2.s.t.
 *              buy[i] = max(buy[i-1], rest[i-1] - prices[i]);
 *              sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
 *              rest[i] = max(rest[i-1], buy[i-1], sell[i-1]);
 *          2.3.for more:
 *              cause of prices[i] >= 0;
 *              so buy[i] <= rest[i] <= sell[i];
 *              s.t.
 *              rest[i] = max(rest[i-1], buy[i-1], sell[i-1]) = sell[i-1];
 *          2.4.Substitute into 2.2:
 *              buy[i] = max(buy[i-1], sell[i-2] - prices[i]);
 *              sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
 *    code base on the transition functions.
 *
 * Complexity:
 *      time: O(N);
 *      space: O(1);
 ***************************************************************/
class Solution1 {
public:
    int maxProfit(vector<int>& prices) {
        int buy_prev = 0, buy = INT_MIN;
        int sell_prev = 0, sell = 0;

        for(int price : prices){
            buy_prev = buy;
            buy = max(buy, sell_prev - price);  //buy[i] = max(buy[i-1], sell[i-2] - prices[i]);
            sell_prev = sell;
            sell = max(sell, buy_prev + price);  //sell[i] = max(sell[i-1], buy[i-1] + prices[i]);
        }

        return sell;
    }
};

/**************************************************************
 * Solution 2:
 *      considering using "state machine".
 *      1.definition of 3 state;
 *          s0: no stock, can buy or rest;
 *          s1: 1 stock, can sell or rest;
 *          s2: no stock, rest -> s0;
 *      2.transition functions:
 *          s0[i] = max(s0[i-1], s2[i-1]);
 *          s1[i] = max(s1[i-1], s0[i-1] - prices[i]);
 *          s2[i] = s1[i-1] + prices[i];
 * Complexity:
 *      time: O(N);
 *      space: O(1);
 ***************************************************************/
class Solution2 {
public:
    int maxProfit(vector<int>& prices) {
        if (prices.size() <= 1) return 0;

        int s0_prev, s0 = 0;
        int s1_prev, s1 = -prices[0];
        int s2_prev, s2 = INT_MIN;

        for(int price : prices){
            s0_prev = s0;
            s1_prev = s1;
            s2_prev = s2;
            s0 = max(s0_prev, s2_prev);  //s0[i] = max(s0[i-1], s2[i-1]);
            s1 = max(s1_prev, s0_prev - price);  //s1[i] = max(s1[i-1], s0[i-1] - prices[i]);
            s2 = s1_prev + price;  //s2[i] = s1[i-1] + prices[i];
        }

        return max(s0, s2);
    }
};

int main() {
    int a[5] = {1,2,3,0,2};
    vector<int> prices(a, a+5);

    Solution1 s1;
    cout << s1.maxProfit(prices) << endl; // prints
    Solution2 s2;
    cout << s2.maxProfit(prices) << endl; // prints

    return 0;
}

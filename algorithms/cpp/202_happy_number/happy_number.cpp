//============================================================================
// Name        : 202_happy_number.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <unordered_set>  //for solution 1
using namespace std;

/************************************************************************
 * Solution 1:
 *      if the sum of squares repeat appears (not 1), it not a happy number;
 *************************************************************************/
class Solution1 {
public:
    bool isHappy(int n) {
        unordered_set<int> nums;  //store the temp value of square_sum;
        int square_sum;

        while(n != 1){
            nums.insert(n);
            square_sum = 0;
            while(n != 0){
                square_sum += (n%10) * (n%10);
                n = n/10;
            }
            if(nums.find(square_sum) != nums.end())
                return false;  //find repeat, not a happy number
            n = square_sum;
        }
        return true;
    }
};

int main() {
    Solution1 s1;
    int num1 = 19;
    cout << s1.isHappy(num1) << endl; // prints
    return 0;
}

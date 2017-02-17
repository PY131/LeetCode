//============================================================================
// Name        : 405_convert_a_number_to_hexadecimal.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <algorithm>  //for reversing a string
using namespace std;

/*****************************************************************
 * Solution:
 *   directly counting for each byte.
 ******************************************************************/
class Solution {
public:
    string toHex(int num) {
        if(num == 0)  return "0";

        string res = "";
        int count = 0, temp;
        while(num != 0 && count < 8){  //set 'count' for 32bit
            temp = num & 15;
            res.push_back( temp < 10 ? '0' + temp: 'a' + temp - 10 );
            num = num >> 4;
            count++;
        }
        reverse(res.begin(), res.end());

        return res;
    }
};

int main() {
    Solution s1;
    int a = 123;
    cout << s1.toHex(a) << endl; // prints
    return 0;
}

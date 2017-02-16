//============================================================================
// Name        : 415_add_strings.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/********************************************************************
 * Solution 1
 *     add by each character.
 *     O(n^2)
 *********************************************************************/
class Solution {
public:
    string addStrings(string num1, string num2) {
        string res = "";
        int carry = 0;  //sum & carry bit

        for(int i = num1.size() - 1, j = num2.size() - 1; i >= 0 || j >= 0 || carry; ){
            if(i >= 0) carry += num1[i--] - '0';
            if(j >= 0) carry += num2[j--] - '0';
            res = to_string(carry%10) + res;
            carry = carry/10;
        }
        return res;
    }
};

int main() {
    Solution s1;
    string num1 = "9", num2 = "99";
    cout << s1.addStrings(num1, num2) << endl; // prints
    return 0;
}

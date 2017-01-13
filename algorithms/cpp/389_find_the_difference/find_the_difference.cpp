//============================================================================
// Name        : 389_find_the_difference.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    char findTheDifference(string s, string t) {
        /*
        * consider XOR to find single number from paired ones
        */
        char diff_ch = s[0];
        string::size_type i;

        for(i = 1; i < s.size(); i++){
            diff_ch ^= s[i];
        }
        for(i = 0; i < t.size(); i++){
            diff_ch ^= t[i];
        }

        return diff_ch;
    }
};

int main() {
    Solution s;
    string s1("abcdmeofg");
    string t1("abcdmefg") ;
    cout << s.findTheDifference(s1, t1) << endl; // prints
    return 0;
}

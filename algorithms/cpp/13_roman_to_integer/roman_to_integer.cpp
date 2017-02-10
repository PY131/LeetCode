//============================================================================
// Name        : 13_roman_to_integer.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <unordered_map>  //for solution 1
using namespace std;

/****************************************************************
 * Solution 1:
 *     Consider using unordered_map for the char-number mapping.
 *****************************************************************/
class Solution1 {
public:
    int romanToInt(string s) {
        if(s.empty()) return 0;
        unordered_map<char, int> res = { {'I', 1},
                                         {'V', 5},
                                         {'X', 10},
                                         {'L', 50},
                                         {'C', 100},
                                         {'D', 500},
                                         {'M', 1000} };
        int sum = res[s.back()];
        for(int i = s.size() - 2; i >= 0; i--){
            if(res[s[i]] < res[s[i+1]]) sum -= res[s[i]];
            else sum += res[s[i]];
        }
        return sum;
    }
};


/****************************************************************
 * Solution 2:
 *     using string's items directly.
 *****************************************************************/
class Solution2 {
public:
    int romanToInt(string s) {
        int sum = 0;
        for(int i = s.size() - 1; i >= 0; i--){
            char c = s[i];
            switch (c){
            case 'I':
                sum += (sum >= 5 ? -1 : 1);
                break;
            case 'X':
                sum += (sum >= 50 ? -10 : 10);
                break;
            case 'C':
                sum += (sum >= 500 ? -100 : 100);
                break;
            case 'M':
                sum += (sum >= 5000 ? -1000 : 1000);  //there is a assumption that sum ~ [0,3999]
                break;
            case 'V':
                  sum += 5;
                  break;
            case 'L':
                  sum += 50;
                  break;
            case 'D':
                  sum += 500;
                  break;
            default:
                cout << "wrong Roman numeral";
                return -1;
            }
        }

        return sum;
    }
};

int main() {
    string s = "MCMLXXX";

    Solution1 s1;
    Solution1 s2;
    cout << s1.romanToInt(s) << endl;
    cout << s2.romanToInt(s) << endl;

    return 0;
}

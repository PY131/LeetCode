//============================================================================
// Name        : 387_first_unique_character_in_a_string.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/**************************************************************
 * we try twice of go through:
 * 1st: count the frequency of each kind of letter
 * 2nd: check the which letter's frequency is first to be once
***************************************************************/
class Solution {
public:
    int firstUniqChar(string s) {
        int i;
        int count[26] = {0};
        //1st:
        for(i = 0; i < s.size(); i++){
        	count[ s[i] - 'a' ]++ ;
        }
        //2nd:
        for(i = 0; i < s.size(); i++){
        	if(count[s[i] - 'a'] <= 1) return i;
        }
        return -1;
    }
};

int main() {
	Solution s;
	string str = "lovvleetcode";

	cout << s.firstUniqChar(str) << endl; // prints
	return 0;
}

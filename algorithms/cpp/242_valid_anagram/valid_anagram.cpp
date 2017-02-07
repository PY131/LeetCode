//============================================================================
// Name        : 242_valid_anagram.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    bool isAnagram(string s, string t) {
        int a[26] = {0};
        int len , i ;
        if(s.size() == t.size()){
            len = s.size();
            for(i = 0; i < len; i++){
                a[s[i] - 'a'] ++;
                a[t[i] - 'a'] --;
            }
            for(i = 0; i < 26; i++){
                if(a[i] != 0) return false;
            }
            return true;
        }
        else return false;
    }
};

int main() {
	Solution s;

	string s1 = "abcd";
	string s2 = "adcb";
	string s3 = "adcs";

	cout << s.isAnagram(s1,s2) << endl; // prints
	cout << s.isAnagram(s1,s3) << endl; // prints

	return 0;
}

//============================================================================
// Name        : 344_reverse_string.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <string>
#include <algorithm>

using namespace std;

class Solution {
public:
    string reverseString(string s) {
    	reverse(s.begin(), s.end());
    	return s;
    }
};

int main() {
	Solution rs1;
	string str1;

	cout << "input:" << endl;
	cin >> str1;

	cout << rs1.reverseString(str1) << endl; // prints
	return 0;
}

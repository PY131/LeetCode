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
    	int i = 0, j = s.size();
    	if(j != 0){
    		while(i < j)  swap(s[i++], s[--j]);
    	}
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

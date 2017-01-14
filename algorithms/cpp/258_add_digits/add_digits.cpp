//============================================================================
// Name        : 258_add_digits.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
	int addDigits(int num) {
		/*
		 * just consider recursive function
		 */
		return num < 10? num: addDigits(num%10 + num/10);
	}
};

int main() {
	Solution s;
	int num;
	cout << "input: " << endl;
	cin >> num;
	cout << "output: " << s.addDigits(num) << endl;
	return 0;
}

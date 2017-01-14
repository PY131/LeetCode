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
		 * refer to the formula of digits root:
		 * 		dr(n) = 1 + ( (n-1) mod 9)
		 *
		 * WikiPedia:
		 * 		https://en.wikipedia.org/wiki/Digital_root
		 * BaiduBaike:
		 * 		http://baike.baidu.com/link?url=KXvH-UnUzkR35gAsZkRTjcCk8LBCnBYZit_LA4A-qqd6JO2B5UkuLgCvBon4mQsTI0C1o6kUDZ2iMJ_RbAxZkq
		 */
		return 1 + (num - 1) % 9;
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

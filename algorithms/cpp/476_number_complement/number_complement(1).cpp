//============================================================================
// Name        : 476_number_complement.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
 #include <math.h>
using namespace std;

class Solution {
public:
    int findComplement(int num) {
    	int mask = ( 1 << ( (int)log2(num) + 1 ) ) - 1 ;	//1st: get the mask of number of bits
    	return ~num & mask;	//2nd: calculation the complement
    }
};

int main() {
	int x1;
	Solution s1;

	cout << "input:" <<endl; // prints
	cin >> x1;
	cout << "output:" << endl; // prints
	cout << s1.findComplement(x1);

	return 0;
}

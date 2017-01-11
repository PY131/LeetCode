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
    	//1st: find the bits number of the num
    	int j = 0, num_temp = num;
    	while (num_temp > 0) {
    		num_temp >>= 1;
    		j++;
    	}
    	//2nd: calculation the complement
    	return pow(2,j) - 1 - num;
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

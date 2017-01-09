//============================================================================
// Name        : number_of_1_bits.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    // you need to treat n as an unsigned value
    int hammingWeight(uint32_t n) {
        int hw = 0;
        while(n!=0){
            if(n%2) hw++;
            n = n>>1;
        }
        return hw;
    }
};

int main() {
	Solution hw1;
	uint32_t x1;
	cout << "input: " << endl;
	cin >> x1;
	cout << "output: ";
	cout << hw1.hammingWeight(x1) << endl;
	return 0;
}

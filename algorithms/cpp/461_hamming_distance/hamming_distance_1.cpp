//============================================================================
// Name        : hamming_distance_1.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    int hammingDistance(int x, int y) {
        int ham_dis = 0;
        while(x!=0 || y!=0){
            if(x%2 != y%2) ham_dis++;
            x = x>>1;
            y = y>>1;
        }
        return ham_dis;
    }
};

int main() {
	Solution hd1;
	int x1, y1;
	cout << "please input two integer: ";
	cin >> x1 >> y1;
	cout << "the hamming distance between this two number is: ";
	cout << hd1.hammingDistance(x1, y1) << endl;;
}

//============================================================================
// Name        : 461_hamming_distance.cpp
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
        int ham_dis, z;
        z = x ^ y;
        for(ham_dis=0; z!=0; z>>=1){
            if(z%2 != 0) ham_dis++;
        }
        return ham_dis;
    }
};

int main() {
	Solution hd1;
	int x1, y1;
	cout << "please input two integers: " << endl;
	cin >> x1 >> y1;
	cout << "the hamming distance is: ";
	cout << hd1.hammingDistance(x1, y1) << endl;;
}

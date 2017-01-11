//============================================================================
// Name        : 292_nim_game.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    bool canWinNim(int n) {
    	//the win possible depended on the distance to 4*i
    	/*
    	 * example: your turn with left number
    	 *  1, 2, 3, win
    	 *  4, lost (you must remove 1~3)
    	 *  5, win (you can reach 4 to make adversary fail)
    	 *  6, win (you can reach 4)
    	 *  7, win (you can reach 4)
    	 *  8, lost (you can not reach 4, but your adversary could)
    	 *  ...(new cycle based on 8)
    	 *  ...(new cycle based on 12)
    	 *  ...
    	 */

        if(n % 4 != 0) return true;
        return false;
    }
};

int main() {
	Solution s1;
	int n1;

	cout <<"input:"<< endl;
	cin >> n1;
	cout << s1.canWinNim(n1) << endl; // prints

	return 0;
}

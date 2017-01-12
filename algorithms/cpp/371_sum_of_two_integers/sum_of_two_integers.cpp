//============================================================================
// Name        : 371_sum_of_two_integers.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    int getSum(int a, int b) {
    	/*
    	 * here we use recursive function
    	 * consider AND for generating bit carry,
    	 *          XOR for generating bit sum without carry;
    	 * for example:
    	 * initial iteration:
    	 *			a(1) = 0 1 0 1
    	 *			b(1) = 1 0 0 1
    	 *		       -----------
    	 *	 a(1) ^ b(1) = 1 1 0 0 -> sum
    	 *	 a(1) & b(1) = 0 0 0 1 -> carry
    	 *
    	 * then:
    	 *		sum -> a(2)
    	 *		(carry << 1) -> b(2)
    	 *		then calculate the sum of a(2) and b(2)
    	 *
    	 * we can use recursive method
    	 * end condition: the carry -> 0, and a(n) is the result;
    	 */

//		int carry;
//
//		carry = (a & b) << 1;
//		a = a ^ b;
//		b = carry;
//
//		return b == 0 ? a : getSum(a, b);

    	return (b == 0) ? a : getSum(a ^ b, (a & b) << 1);
    }
};

int main() {
	int a1, b1;
	Solution s;

	cout << "input two integers:" << endl;
	cin >> a1 >> b1;
	cout << "the sum is: " << s.getSum(a1, b1) << endl;

	return 0;
}

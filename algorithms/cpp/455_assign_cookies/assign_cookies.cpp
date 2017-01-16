//============================================================================
// Name        : 455_assign_cookies.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

class Solution {
public:
    int findContentChildren(vector<int>& g, vector<int>& s) {
    	int c = 0;

    	/*
    	 * at first: sort the vector.
    	 * then: compare them from small to big in sequence.
    	 */
    	std::sort (g.begin(), g.end());
    	std::sort (s.begin(), s.end());

    	for(vector<int>::size_type i = 0, j = 0; i < g.size() && j < s.size(); ){
    		if(s[j] >= g[i]){
    			c++, i++, j++;
    		}
    		else j++;
    	}

    	return c;
    }
};

int main() {
	Solution s;

	vector<int> g1 = {4,2,1,4,5};
	vector<int> s1 = {4,2,1,3};

	cout << s.findContentChildren(g1, s1) << endl; // prints
	return 0;
}

//============================================================================
// Name        : 383_ransom_note.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

class Solution {
public:
    bool canConstruct(string ransomNote, string magazine) {
    	/*
    	 * consider using array<int> to count the number of each letter
    	 * then check: magazine's each letter's number must no less than ransomNote's
    	 * the runtime is O(m+n)
    	 */
    	string::size_type i;
    	int count[26] = {0};  //26 lowercase letters

    	for(i = 0; i < magazine.length(); i++){
    		count[magazine[i] - 'a']++;
    	}
    	for(i = 0; i < ransomNote.length(); i++){
    		if((--count[ransomNote[i] - 'a']) < 0) return false;
    	}
    	return true;
    }
};

int main() {
	string a = "ads";
	string b = "aabs";
	Solution s;

	cout << s.canConstruct(a, b) << endl; // prints
	return 0;
}

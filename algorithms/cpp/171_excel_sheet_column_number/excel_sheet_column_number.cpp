//============================================================================
// Name        : 171_excel_sheet_column_number.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

/**********************************************************
 * consider using reverse-recursion object to 168's Solution
 ***********************************************************/
class Solution1 {
public:
    int titleToNumber(string s) {
		int n = 0;

		if(s == "") return 0;

		n += ( *(s.end() - 1) - 'A') + 1;
		s.pop_back();  //remove the last char
		return n += titleToNumber(s) * 26;
    }
};

/**********************************************************
 * the 2nd solution using while loop object to 168's Solution2
 ***********************************************************/
class Solution2 {
public:
    int titleToNumber(string s) {
		int n = 0;

		for(unsigned int i = 0; i < s.size(); i++){
			n = n * 26 + (s[i] - 'A') + 1;
		}
		return n;
    }
};

int main() {
	Solution2 s1;
	string s = "AB";

	cout << s1.titleToNumber(s) << endl; // prints

	return 0;
}

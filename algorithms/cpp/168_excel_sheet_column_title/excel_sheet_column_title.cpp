//============================================================================
// Name        : 168_excel_sheet_column_title.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
using namespace std;

#include <string>

/************************************************************
 * Consider recursive with divider and reminder
 *************************************************************/
class Solution {
public:
    string convertToTitle(int n) {
    	string s = "";

    	if(n == 0) return s;
    	s.insert( s.begin(), 'A' + (n - 1)%26 );
    	s.insert( 0, convertToTitle( (n - 1)/26 ) );

    	return s;
    }
};

/************************************************************
 * Solution2: consider using while loop
 * refer to: http://www.cplusplus.com/reference/string/string/operator+/
 *************************************************************/
class Solution2 {
public:
    string convertToTitle(int n) {
    	string s = "";

    	while( n != 0 ){
        	s = char('A' + (n - 1) % 26) + s;  //directly using overloaded operator "+" for string inserting
        	n = (n - 1) / 26;
    	}

    	return s;
    }
};

int main() {
	Solution2 s;

	cout << s.convertToTitle(30) << endl; // prints
	return 0;
}

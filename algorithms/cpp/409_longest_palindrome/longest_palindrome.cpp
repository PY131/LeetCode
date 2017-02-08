//============================================================================
// Name        : 409_longest_palindrome.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <unordered_map>  //for solution 2
using namespace std;

/****************************************************************
 * Solution 1:
 *     1st. using index counting the numbers of each character.
 *     2nd. calculating the length of palindrome by checking
 *          whether the number is odd or even.
 *****************************************************************/
class Solution1 {
public:
    int longestPalindrome(string s) {
    	int arr[256] = {0};  //the counting of all characters
    	int len = 0;
    	bool flag = 0;  //checking whether the odd one is added

    	for(string::size_type i = 0; i < s.size(); i++){
    		arr[s[i] - '\0'] ++;
    	}

    	for(int i = 0; i < 256; i++){
    		if(arr[i] != 0){
    			if(flag == 0){  //the odd is uncounted
    				if(arr[i]%2){  //checking if is odd
    					len += 1 + 2 * ( arr[i]/2 );
    					flag = 1;
    				}
    				else len += arr[i];
    			}
    			else len += 2 * ( arr[i]/2 );
    		}
    	}

    	return len;
    }
};

/****************************************************************
 * Solution 2:
 *     consider using unordered_map for counting.
 *****************************************************************/
class Solution2 {
public:
    int longestPalindrome(string s) {
        int len = 0;
    	unordered_map<char, int> counts;

    	for(string::size_type i = 0; i < s.size(); i++){
    		if( counts.find(s[i]) != counts.end() ){  //check to see whether is odd or even
            	len += 2;
            	counts.erase(s[i]);
            }
    		else counts.insert( unordered_map<char, int>::value_type(s[i], 0));
        }
        if(!counts.empty()) len++;  //item left means odd existed

        return len;
    }
};

int main() {
	string s = "abccccdd";

	Solution1 s1;
	Solution2 s2;
	cout << s1.longestPalindrome(s) << endl; // prints
	cout << s2.longestPalindrome(s) << endl; // prints

	return 0;
}

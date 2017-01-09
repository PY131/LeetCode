//============================================================================
// Name        : fizz_buzz.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>

using namespace std;

class Solution {
public:
    vector<string> fizzBuzz(int n) {
        vector<string> str_vec;
        for(int i=1; i<=n; i++){
        	if(i%3 == 0 && i%5 == 0) str_vec.push_back("FizzBuzz");
        	else if(i%3 == 0) str_vec.push_back("Fizz");
        	else if(i%5 == 0) str_vec.push_back("Buzz");
        	else str_vec.push_back(to_string(i));
        }
        return str_vec;
    }
};

int main() {
	Solution fb1;
    vector<string> str_vec1;
	int n;

	cout << "input:" << endl;
	cin >> n;
	str_vec1 = fb1.fizzBuzz(n);
	cout << "output:"<<endl;
	for (int i = 0; i < n; i++)
    {
        cout <<str_vec1[i]<<endl;
    }
}

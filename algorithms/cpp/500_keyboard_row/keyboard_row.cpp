//============================================================================
// Name        : 500_keyboard_row.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <unordered_set>
using namespace std;

/**************************************************************
 * Solution 1:
 *      comparing for each words
 ***************************************************************/
class Solution1 {
public:
    vector<string> findWords(vector<string>& words) {
        vector<unordered_set<char>> rows{
            {'q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'},
            {'a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'},
            {'z', 'x', 'c', 'v', 'b', 'n', 'm'}
        };
        vector<string> valid_words;
        int i;
        bool flag;

        for(string word : words){  //analysis one by one.
            flag = true;
            for(i = 0; i < 3; i++){
                if(rows[i].count( tolower(word[0]) ) > 0 ) break;  //check which row oughts to belong
            }
            for(char ch : word){
                if(rows[i].count( tolower(ch) ) == 0 ){
                    flag = false;
                    break;
                }
            }
            if(flag) valid_words.push_back(word);
        }
        return valid_words;
    }
};

/*********************************************
 * Function:
 *     printing vector
 *********************************************/
template<class T>
void print_vec(vector<T>& res){
    for(auto it : res){
        cout << it <<" "; // prints
    }
    cout << endl;
    return;
}

int main() {
    vector<string> words {"Hello","Alaska","Dad","Peace"};

    Solution1 s1;
    vector<string> res = s1.findWords(words);
    print_vec(res);
    return 0;
}

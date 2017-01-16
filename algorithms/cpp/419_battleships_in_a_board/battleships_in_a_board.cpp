//============================================================================
// Name        : 419_battleships_in_a_board.cpp
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
    int countBattleships(vector<vector<char>>& board) {
        int c = 0;

        /*
         * here we just check whether the X is the head of a ship
         * head means: the far left or the top;
         */
        vector<int>::size_type m = board.size();
        vector<int>::size_type n = board[0].size();
        vector<int>::size_type i, j;

        for(i = 0; i < m; i++){
            for(j = 0; j < n; j++){
                if(board[i][j] == 'X'){
                    if(i > 0 && board[i-1][j] == 'X') continue;  //AND operation, once false, ignore the rests
                    if(j > 0 && board[i][j-1] == 'X') continue;
                    c++;
                }
            }
        }
        return c;
    }
};

int main() {
    //preparing data matrix
    char a[][5] = {
        "X..X",
        "X..X",
        "...X",
        "X..X"
    };
    vector<vector<char>> board(4);
    for(int i = 0; i < 4; i++){
        board[i].assign(a[i], a[i]+4);
    }

    Solution s;
    cout << s.countBattleships(board) << endl; // prints

    return 0;
}

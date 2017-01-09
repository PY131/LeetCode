//============================================================================
// Name        : 463_island_perimeter.cpp
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
    int islandPerimeter(vector<vector<int>>& grid) {
    	int sp = 0;
    	vector<int>::size_type m, n, i, j;

    	m = grid.size();
    	n = grid[0].size();

		for(i = 0; i < m; i++){
			for(j = 0; j < n; j++)
			{
				if(grid[i][j] == 1){
					{
						if(i == 0) sp++;
						else if(grid[i-1][j] == 0) sp++;
					}
					{
						if(i == m-1) sp++;
						else if(grid[i+1][j] == 0) sp++;
					}
					{
						if(j == 0) sp++;
						else if(grid[i][j-1] == 0) sp++;
					}
					{
						if(j == n-1) sp++;
						else if(grid[i][j+1] == 0) sp++;
					}
				}
			}
		}
    	return sp;
    }
};

int main() {
	Solution ip1;
	vector<vector<int>> grid_1 = {	{0,1,0,0},
									{1,1,1,0},
									{0,1,0,0},
									{1,1,0,0}};
	cout << ip1.islandPerimeter(grid_1) << endl; // prints

	return 0;
}

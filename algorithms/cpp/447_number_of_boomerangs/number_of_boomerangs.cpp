//============================================================================
// Name        : 447_number_of_boomerangs.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <unordered_map>
using namespace std;

/***************************************************************
* Soultion 1:
*   count each distance in a vertex directly
* Complexity:
*   time:  O(N*N); 
*   space: O(N);
****************************************************************/
class Solution {
public:
    int numberOfBoomerangs(vector<pair<int, int>>& points) {
        unordered_map<long, int> dis2(points.size());  //key is distance's square and value is counts
        int res = 0;

        int dis_ij_2, dx, dy;
        for(int i = 0; i < points.size(); i++){
            for(int j = 0; j < points.size(); j++){
                dx = points[i].first - points[j].first;
                dy = points[i].second - points[j].second;
                dis_ij_2 = dx*dx + dy*dy;
                dis2[dis_ij_2]++;
            }
            for(auto it : dis2){
                if(it.first != 0 ) res += it.second * (it.second - 1);  //Permutation
            }
            dis2.clear();
        }

        return res;
    }
};

int main() {
    pair<int,int> psi[3];
    for (int i = 0; i < 3; i++){
        psi[i] = make_pair(i,0);
    }
    vector<pair<int, int>> points(psi, psi+3);
//    for(auto it : points){
//        cout << it.first << " " << it.second <<" "; // prints
//    }
//    cout << endl;

    Solution s1;
    cout << s1.numberOfBoomerangs(points) << endl; // prints
    return 0;
}

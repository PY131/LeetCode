//============================================================================
// Name        : 401_binary_watch.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
using namespace std;

/******************************************************************
 * Solution 1:
 *    traversal to check the digit 1 numbers
 *******************************************************************/
class Solution1 {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> times;

        for(int h = 0; h < 12; h++){
            for(int m = 0; m < 60; m++){
                if(bitcount(h) + bitcount(m) == num){
                    times.push_back( to_string(h) + (m < 10 ?  ":0" : ":") + to_string(m) );  //insert a new possible time
                }
            }
        }
        return times;
    }

private:
    int bitcount(unsigned x){  //counting the 1 bit numbers in a integer
        int b;
        for (b = 0; x != 0; x &= (x-1)) b++;
        return b;
    }
};

/******************************************************************
 * Solution 2:
 *     consider using [Backtracking]
 *******************************************************************/
class Solution2 {
public:
    vector<string> readBinaryWatch(int num) {
        vector<string> times;
        vector<int> nums1 = {8, 4, 2, 1};
        vector<int> nums2 = {32, 16, 8, 4, 2, 1};

        for(int i = 0; i <= num; i++) {
            vector<int> times_h = sub_read(nums1, i);
            vector<int> times_m = sub_read(nums2, num - i);
            for(int h: times_h) {
                if(h >= 12) continue;
                for(int m: times_m) {
                    if(m >= 60) continue;
                    times.push_back( to_string(h) + (m < 10 ? ":0" : ":") + to_string(m) );
                }
            }
        }
        return times;
    }

private:
    vector<int> sub_read(vector<int> &nums, int count){
        vector<int> times;
        sub_read_rec(nums, count, 0, 0, times);
        return times;
    }

    void sub_read_rec(vector<int> &nums, int count, int pos, int sum, vector<int> &times){
        if(count == 0){
            times.push_back(sum);
            return;
        }
        for(vector<int>::size_type i = pos; i < nums.size(); i++) {
            sub_read_rec(nums, count - 1, i + 1, sum + nums[i], times);
        }
    }
};

int main() {
    Solution1 s1;
    Solution2 s2;
    vector<string> times;

    times = s1.readBinaryWatch(1);
    for(vector<int>::size_type i = 0; i < times.size(); i++){
        cout << times[i] << endl; // prints
    }

    times = s2.readBinaryWatch(1);
    for(vector<int>::size_type i = 0; i < times.size(); i++){
        cout << times[i] << endl; // prints
    }
	return 0;
}

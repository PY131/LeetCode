//============================================================================
// Name        : 350_intersection_of_two_arrays_II.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>  // for std::sort, std::set_intersection.
#include <unordered_map>  //for Solution 2
using namespace std;

/**********************************************************************
 * Solution 1:
 *     sorting & using "set_intersection"
 * Complexity:
 *     time:  O(N*lgN)
 *     space: O(N)
 ***********************************************************************/
class Solution1 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res(nums1.size() + nums2.size());
        vector<int>::iterator it;

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        it = set_intersection(nums1.begin(), nums1.end(), nums2.begin(), nums2.end(), res.begin());
        res.resize(it - res.begin());

        return res;
    }
};

/**********************************************************************
 * Solution 2:
 *     using hash_map's key-value for counting
 * Complexity:
 *     time:  O(N+M)
 *     space: O(min(N,M))
 ***********************************************************************/
class Solution2 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;
        unordered_map<int, int> count;

        for(vector<int>::size_type i = 0; i < nums1.size(); i++){
            count[nums1[i]]++;
        }
        for(vector<int>::size_type i = 0; i < nums2.size(); i++){
            if(count.find(nums2[i]) != count.end() && --count[nums2[i]] >= 0)
                res.push_back(nums2[i]);
        }

        return res;
    }
};

/**********************************************************************
 * Solution 3:
 *     we can compare directly after sorting
 * Complexity:
 *     time:  O(N+M)
 *     space: O(min(N,M))
 ***********************************************************************/
class Solution3 {
public:
    vector<int> intersect(vector<int>& nums1, vector<int>& nums2) {
        vector<int> res;

        sort(nums1.begin(), nums1.end());
        sort(nums2.begin(), nums2.end());

        for(vector<int>::size_type i1 = 0, i2 = 0; i1 < nums1.size() && i2 < nums2.size(); ){
            if(nums1[i1] == nums2[i2]) {
                res.push_back(nums1[i1]);
                i1++;
                i2++;
            }
            else{
                if(nums1[i1] < nums2[i2]) i1++;
                else i2++;
            }
        }

        return res;
    }
};

/*********************************************
 * Function:
 *     printing vector
 *********************************************/
void print_vec(vector<int>& res){
    for(auto it : res){
        cout << it <<" "; // prints
    }
    cout << endl;
    return;
}

int main() {
    int first[] = {20,10,5,20};
    int second[] = {50,30,20,10,40};

    vector<int> nums1(first, first + 4);
    vector<int> nums2(second, second + 5);
    vector<int> res;

    Solution1 s1;
    Solution2 s2;
    Solution3 s3;

    res = s1.intersect(nums1, nums2);
    print_vec(res);
    res = s2.intersect(nums1, nums2);
    print_vec(res);
    res = s3.intersect(nums1, nums2);
    print_vec(res);

    return 0;
}

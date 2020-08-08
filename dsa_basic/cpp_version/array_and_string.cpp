#include "array_and_string.h"
#include <iostream>

vector<int> ArrayString::twoSum(vector<int>& nums, int target) {
    // force-brute O(n^2)
    // using a map to reduce O(n) with space O(n)
    // map k: num, v: [index]
    vector<int> res;

    unordered_map<int, vector<int>> M;
    for (int i = 0; i < nums.size(); i++) {
        int x = nums[i];
        if (M.find(x) != M.end()) {
            M[x].push_back(i);
        } else {
            vector<int> tmp = {i};
            M.insert(make_pair(x, tmp));
        }
    }
    for (int i = 0; i < nums.size(); i++) {
        int tar = target - nums[i];
        if (M.find(tar) != M.end()) {
            int tar_idx = M[tar][0];
            if (tar_idx == i) {
                if (M[tar].size() > 1) {
                    tar_idx = M[tar][1];
                } else {
                    continue;
                }
            }
            res.push_back(i);
            res.push_back(tar_idx);
            break;
        }
    }
    return res;
}

double ArrayString::findMedianSortedArrays(vector<int>& nums1, vector<int>& nums2) {
    // set the middle number can mark as nums1[0,.,m1,.,n1-1] and nums2[0,.,m2,.,n2-1]
    // while m2 = (n1 + n2 - 3) / 2 - m1, if m1 ~ [0, n1), m2 ~ [0, n2)
    // the final status is that nums1[m1] < nums2[m2 + 1] and nums[m2] < nums[m1 + 1]
    // then return the middle from m1, m2, m1+1, m2+1
    int n1 = nums1.size();
    int n2 = nums2.size();

    vector<int>& arr1 = nums1;
    vector<int>& arr2 = nums2;
    if (n1 < n2) {
        vector<int>& tmp = arr1;
        arr1 = arr2;
        arr2 = tmp;
    }

    int lo = 0;
    int hi = n1 - 1;

    while (lo < hi) {
        int m1 = lo + (hi - lo + 1) / 2;
        int m2 = (n1 + n2 - 3) / 2 - m1;
        int left2 = INT_MIN;
        int right2 = INT_MAX;
        if (m2 >= 0) {
            left2 = arr2[m2];
        }
        if (m2 + 1 < n2) {
            right2 = arr2[m2 + 1];
        }
        if (arr1[m1] <= right2) {
            lo = m1;
        } else {
            hi = m1 - 1;
        }
    }
    
    double res;
    int m1 = lo;
    int m2 = (n1 + n2 - 3) / 2 - m1;
    if ((n1 + n2) % 2 == 1) {
        res = max(arr1[m1], arr2[m2]);
    } else {
        res = 1.0 * (max(arr1[m1], arr2[m2]) + min) / 2;
    }
    return res;
}

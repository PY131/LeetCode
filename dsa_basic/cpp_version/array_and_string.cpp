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
    int n1 = nums1.size();
    int n2 = nums2.size();
    int n_left = (n1 + n2 + 1) / 2;
    int lo = 0;
    int hi = n1 - 1;
    while (lo < hi) {
        int m1 = lo + (hi - lo + 1) / 2;
        int m2 = n_left - (m1 + 1) - 1;
        int l1 = INT_MIN;
        int r1 = INT_MAX;
        int l2 = INT_MIN;
        int r2 = INT_MAX;
        if (m1 >= 0)        l1 = nums1[m1];
        if (m1 + 1 < n1)    r1 = nums1[m1 + 1];
        if (m2 >= 0)        l2 = nums2[m2];
        if (m2 + 1 < n2)    r2 = nums2[m2 + 1];
        if (l1 < r2) {
            lo = m1;
        } else {
            hi = m1 - 1;
        }
    }
    int m1 = lo;
    int m2 = n_left - (m1 + 1) - 1;
    int l1 = INT_MIN;
    int r1 = INT_MAX;
    int l2 = INT_MIN;
    int r2 = INT_MAX;
    if (m1 >= 0)        l1 = nums1[m1];
    if (m1 + 1 < n1)    r1 = nums1[m1 + 1];
    if (m2 >= 0)        l2 = nums2[m2];
    if (m2 + 1 < n2)    r2 = nums2[m2 + 1];
    double res;
    if ((n1 + n2) % 2 == 1) {
        res = max(l1, l2);
    } else {
        res = 0.5 * (max(l1, l2) + min(r1, r2));
    }
    return res;
}

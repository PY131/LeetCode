#include <iostream>
#include "dp.h"

int DP::fibonacci(int n) {
    // f[i] = f[i - 1] + f[i - 2]
    int f0 = 0;
    int f1 = 1;
    while (n--) {
        f1 = f1 + f0;
        f0 = f1 - f0;
    }
    return f0;
}

int DP::max_sum_of_subarray(std::vector<int> & array) {
    if (array.size() == 0) {
        return 0;
    }
    int res = array[0];
    int dp = array[0];
    for (size_t i = 1; i < array.size(); i++) {
        // dp[i] = max(arr[i], dp[i-1] + arr[i])
        dp = std::max(array[i], array[i] + dp);
        if (res < dp) {
            res = dp;
        }
    }
    return res;
}

void DP::print_array(std::vector<int> & array) {
    for (auto x : array) {
        std::cout << x << ", ";
    }
    std::cout << std::endl;
}

int DP::length_of_LIS(std::vector<int> & array) {
    std::vector<int> tmp;
    for (int x : array) {
        // find the smallest index in array that array[idx] >= x
        // then we set array[idx + 1] = x
        int lo = 0;
        int hi = tmp.size() - 1;
        if (hi < lo || x > tmp[hi]) {
            tmp.push_back(x);
            continue;
        }
        while (lo < hi) {
            int mi = lo + (hi - lo) / 2;
            if (tmp[mi] < x) {
                lo = mi + 1;
            } else {
                hi = mi;
            }
        }
        tmp[lo] = x;
    }
    return tmp.size();
}
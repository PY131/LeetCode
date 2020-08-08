#pragma once
#include <vector>

class DP {
  public:
    int fibonacci(int n);
    // max sum of continuous sub array
    int max_sum_of_subarray(std::vector<int> &array);
    // longest increasing subsequence.
    int length_of_LIS(std::vector<int> & array);

  private:
    void print_array(std::vector<int> & array);
};
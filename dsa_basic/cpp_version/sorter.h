#pragma once
#include <vector>
#include <string>

using namespace std;

class Sorter {
  public:
    void bubble_sort(std::vector<int> & array);
    void quick_sort(std::vector<int> & array);
    void merge_sort(std::vector<int> & array);
    void heap_sort(std::vector<int> & array);

    void show_array(std::vector<int> & array, const std::string & prefix);

  private:
    void quick_sort(std::vector<int> & array, int lo, int hi);
    void merge_sort(std::vector<int> & array, int lo, int hi, std::vector<int> & tmps);
    void merge_two(std::vector<int> & array, int lo, int hi, int mi, std::vector<int> & tmps);
    void heap_build(std::vector<int> & array);
    void heap_adjust(std::vector<int> & array, int p, int hi);

    template <typename T>
    void swap(std::vector<T> & array, int i, int j);
};

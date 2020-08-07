#include <iostream>
#include "sorter.h"

template <typename T>
void Sorter::swap(std::vector<T> & array, int i, int j) {
    T tmp = array[i];
    array[i] = array[j];
    array[j] = tmp;
}

void Sorter::bubble_sort(std::vector<int> & array) {
    for (size_t i = 0; i < array.size(); i ++) {
        bool flag = false;
        for (size_t j = 1; j < array.size() - i; j ++) {
            if (array[j-1] > array[j]) {
                int tmp = array[j-1];
                array[j-1] = array[j];
                array[j] = tmp;
                flag = true;
            }
        }
        if (!flag) {
            break;
        }
    }
    return;
}

void Sorter::quick_sort(std::vector<int> & array) {
    quick_sort(array, 0, array.size() - 1);
}

void Sorter::quick_sort(std::vector<int> & array, int lo, int hi) {
    if (hi - lo < 1) { return; }
    int i = lo;
    int j = hi;
    int tar = array[lo];
    while (i < j) {
        while (i < j && array[j] >= tar) { j -= 1; }
        array[i] = array[j];
        while (i < j && array[i] <= tar) { i += 1; }
        array[j] = array[i];
    }
    array[i] = tar;
    quick_sort(array, lo, i - 1);
    quick_sort(array, i + 1, hi);
    return;
}

void Sorter::merge_sort(std::vector<int> & array) {
    std::vector<int> tmps;
    tmps.resize(array.size());
    merge_sort(array, 0, array.size() - 1, tmps);
}

void Sorter::merge_sort(std::vector<int> & array, int lo, int hi, std::vector<int> & tmps) {
    if (hi - lo < 1) { return; }
    // partition
    int mi = lo + (hi - lo) / 2;
    merge_sort(array, lo, mi, tmps);
    merge_sort(array, mi + 1, hi, tmps);
    // merge
    merge_two(array, lo, hi, mi, tmps);
}

void Sorter::merge_two(std::vector<int> & array, int lo, int hi, int mi, std::vector<int> & tmps) {
    int p = lo;
    int i = lo;
    int j = mi + 1;
    while (i <= mi && j <= hi) {
        if (array[i] <= array[j]) {
            tmps[p++] = array[i++];
        } else {
            tmps[p++] = array[j++];
        }
    }
    while (i <= mi) {
        tmps[p++] = array[i++];
    }
    while (j <= hi) {
        tmps[p++] = array[j++];
    }
    for (int k = lo; k <= hi; k++) {
        array[k] = tmps[k];
    }
    return;
}

void Sorter::heap_sort(std::vector<int> & array) {
    heap_build(array);
    for (int i = array.size() - 1; i > 0; i--) {
        swap(array, i, 0);
        heap_adjust(array, 0, i - 1);
    }
}

void Sorter::heap_build(std::vector<int> & array) {
    for (int i = (array.size() - 2) / 2; i >= 0; i--) {
        heap_adjust(array, i, array.size() - 1);
    }
}

void Sorter::heap_adjust(std::vector<int> & array, int p, int hi) {
    // for max heap
    while (p < hi) {
        int lc = 2 * p + 1;
        int rc = 2 * p + 2;
        int k = lc;
        if (rc <= hi && array[rc] > array[lc]) {
            k = rc;
        }
        if (k <= hi && array[k] > array[p]) {
            swap(array, k, p);
            p = k;
        } else {
            break;
        }
    }
}

void Sorter::show_array(std::vector<int> & array, const std::string & prefix) {
    std::cout << prefix;
    for (size_t i = 0; i < array.size(); i++) {
         std::cout << array[i] << ",";
    }
    std::cout << std::endl;
}

//============================================================================
// Name        : 215_kth_largest_element_in_an_array.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <algorithm>
#include <queue>

using namespace std;

class Solution {
public:

    /*********************************************************
     * Solution 1: using quick sort to all elements
     *
     * @function: findKthLargest_1.
     * @description: return the k_th largest element in an array.
     *
     * @parameters:
     *      nums: vector<int>, number array.
     *      k: int, order
     * @return:
     *      int, the k_th largest element
     * @complexity:
     *      time: O(n*lgn).
     **********************************************************/
    int findKthLargest_1(vector<int>& nums, int k) {
        sort(nums.begin(), nums.end());
        return nums[nums.size() - k];
    }

    /*********************************************************
     * Solution 2: using quick select (partition and selection)
     *
     * @function: findKthLargest_2.
     * @description: return the k_th largest element in an array.
     *
     * @parameters:
     *      nums: vector<int>, number array.
     *      k: int, order
     * @return:
     *      int, the k_th largest element
     *
     * @complexity:
     *      time: O(k*n), best O(n), worst O(n^2).
     **********************************************************/
    int findKthLargest_2(vector<int>& nums, int k) {
        int left = 0, right = nums.size() - 1;
        int pos;
        while(1) {
            pos = partition(nums, left, right);
            if(pos == k-1) return nums[pos];
            else if(pos < k-1) left = pos + 1;
            else right = pos - 1;
        }
    }

    /*********************************************************
     * helper function for solution 2
     *
     * @function: partition.
     * @description: partition an array from left to right.
     *               so that. (big to smaller)
     *               nums[left,j) > nums[j] > nums[j+1, right].
     *               initial pivot as nums[left].
     * @parameters:
     *      nums: vector<int>, number array.
     *      left: int, start index of sub-array.
     *      right:int, end index of sub-array. lenght - 1.
     * @return:
     *      int, the j's index after partition
     **********************************************************/
    int partition(vector<int>& nums, int left, int right) {
        int pivot = nums[left];
        int i = left + 1;
        int j = right;
        while(i <= j) {
            if(nums[i] < pivot && nums[j] > pivot) {
                swap(nums[i++], nums[j--]);
            }
            if(nums[i] >= pivot) i++;
            if(nums[j] <= pivot) j--;
        }
        swap(nums[left], nums[j]);

        return j;  // return the partition index
    }

    /*********************************************************
     * Solution 3: using Heap Sort (max-heap)
     *
     * @function: findKthLargest_3.
     * @description: return the k_th largest element in an array.
     *
     * @parameters:
     *      nums: vector<int>, number array.
     *      k: int, order
     * @return:
     *      int, the k_th largest element
     *
     * @complexity:
     *      time: O(nlgn), we can just build max_head with size k.
     **********************************************************/
    int findKthLargest_3(vector<int>& nums, int k) {
        priority_queue<int> pq(nums.begin(), nums.end());
        for (int i = 0; i < k - 1; i++)
            pq.pop();
        return pq.top();
    }

};


// print vector
void print_vec(vector<int>& nums) {
    for (auto val : nums)   cout << val << ' ';
    cout << endl;
    return;
}

// test code
int main() {
    int data[] = {3,2,1,5,6,4};
    vector<int> nums(data, data + 6);
    print_vec(nums);

    Solution s;
    int k_th = s.findKthLargest_3(nums, 2);

    print_vec(nums);
    cout << "k_th largest element is: " << k_th << endl;
    return 0;
}

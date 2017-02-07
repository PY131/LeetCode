//============================================================================
// Name        : 169_majority_element.cpp
// Author      : PY131
// Version     :
// Copyright   : 
// Description : Hello World in C++, Ansi-style
//============================================================================

#include <iostream>
#include <vector>
#include <unordered_map>  //for solution 2
#include <time.h>  //for solution 3
#include <algorithm> //for solution 4
using namespace std;

/*****************************************************************
 * Solution 1:
 *     consider the majority element' count is bigger than the sum of others'
 * method:
 *     offset the different elements and the majority ones is left at end
*****************************************************************/
class Solution1 {
public:
    int majorityElement(vector<int>& nums) {
        int count = 0, major;

        for(vector<int>::size_type i = 0; i < nums.size(); i++){
            if(count == 0){
                major = nums[i];
                count = 1;
            }
            else if(major != nums[i]) count--;
            else count++;
        }

        return major;
    }
};

/*****************************************************************
 * Solution 2:
 *     using unordered map (STL container) which is high effective
 *****************************************************************/
class Solution2 {
public:
    int majorityElement(vector<int>& nums) {
        unordered_map<int, int> counts;  //the definition of unordered map (hash map)
        int n = nums.size();

        for(int i = 0; i < n; i++){
            if( ++ counts[ nums[i] ] > n/2 ){  //added the value using the nums[] as the key
                return nums[i];
            }
        }
        return -1;
    }
};

/******************************************************************
 * Solution 3:
 *     using random approach
 * principle:
 *     cause of the majority item always exist,
 *     the possibility (p) of random seed fall down on it is bigger than 1/2.
 *     so, we can directly counting the random selected one to see if is the majority one
 *     the expectation of computing complexity is:
 *         E(O) = p*O(N) + (p*(1-p))*(2*O(N)) + (p*(1-p)^2)*(3*O(N)) ...
 *              = Sigma( (p * (1-p)^(n-1)) * n * O(N) , n = 1,2,3...+inf;
 *         as p > 0.5
 *     so the E(O) ~ O(N) which proof to be high effective
 ******************************************************************/
class Solution3 {
public:
    int majorityElement(vector<int>& nums) {
         int r, i, major, count;
         int n = nums.size();
         srand(unsigned(time(0)));  //initial a rand seed

         while(1){
             r = rand() % n;  //create a rand number
             major = nums[r];
             count = 0;
             for(i = 0; i < n; i++){
                if(nums[i] == major)  count++;
             }
             if(count > n/2) return major;
         }
    }
};

/******************************************************************
 * Solution 4:
 *     using [Divide and Conquer] algorithm
 * method:
 *     using recursion to divide the N to 1;
 ******************************************************************/
class Solution4 {
public:
    int majorityElement(vector<int>& nums) {
        return majority(nums, 0, nums.size() - 1);
    }
private:
    int majority(vector<int> &nums, int left, int right){
        if(left == right) return nums[left];
        int mid = left + ((right - left) >> 1);
        int lm = majority(nums, left, mid);
        int rm = majority(nums, mid + 1, right);
        if(lm == rm)  return lm;
        else return count(nums.begin() + left, nums.begin() + right + 1, lm) > count(nums.begin() + left, nums.begin() + right + 1, rm)? lm : rm;
    }
};


int main() {
	int a[10] = {0,0,0,1,0,1,0,1,1,0};
	vector<int> nums(&a[0], &a[9]);

	Solution1 s1;
	Solution2 s2;
	Solution3 s3;
	Solution4 s4;

	cout << s1.majorityElement(nums) << endl;
	cout << s2.majorityElement(nums) << endl;
	cout << s3.majorityElement(nums) << endl;
	cout << s4.majorityElement(nums) << endl;

	return 0;
}

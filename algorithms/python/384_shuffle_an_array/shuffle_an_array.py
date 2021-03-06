# coding: utf8
# python 2.7
"""
Link: Shuffle a set of numbers without duplicates.

Example:

    // Init an array with set 1, 2, and 3.
    int[] nums = {1,2,3};
    Solution solution = new Solution(nums);

    // Shuffle the array [1,2,3] and return its result. Any permutation of [1,2,3] must equally likely to be returned.
    solution.shuffle();

    // Resets the array back to its original configuration [1,2,3].
    solution.reset();

    // Returns the random shuffling of array [1,2,3].
    solution.shuffle();
"""
from copy import deepcopy
from random import randrange

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums
        self.original = deepcopy(nums)
        self.len = len(nums)

    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.original

    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        :using knuth shuffle idea
        """
        for i in range(self.len-1, -1, -1):
            r = randrange(i+1)
            self.nums[i], self.nums[r] = self.nums[r], self.nums[i]
        return self.nums

 
if __name__ == "__main__":
    nums = [1,2,3,4,5]
    obj = Solution(nums)
    param_1 = obj.reset()
    param_2 = obj.shuffle()
    print param_2, param_1


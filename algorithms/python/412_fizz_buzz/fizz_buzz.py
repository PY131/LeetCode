# coding: utf8
# python 2.7
"""
Link: https://leetcode-cn.com/problems/fizz-buzz
Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz” instead of the number 
and for the multiples of five output “Buzz”. 
For numbers which are multiples of both three and five output “FizzBuzz”.

Example:
    n = 15,
    Return:
    [ "1", "2", "Fizz", "4", "Buzz", "Fizz", 
      "7", "8", "Fizz", "Buzz", "11", "Fizz", 
      "13", "14", "FizzBuzz"]
"""
from collections import OrderedDict
class Solution(object):

    def fizzBuzz(self, n):
        """idea: using a map to record the target num and check for concat the string
        """
        M = OrderedDict([
            (3, 'Fizz'), 
            (5, 'Buzz')
        ])
        res = []
        for i in range(1, n+1):
            item = ''
            for k in M:
                if i % k == 0:
                    item += M[k]
            if not item:
                item = str(i)
            res.append(item)
        return res

    def fizzBuzz_v1(self, n):
        """
        :type n: int
        :rtype: List[str]
        :idea: naive way, just go-ahead one-by-one
        :complexity: time: O(n), space: O(n)
        """
        res = []
        for i in range(1, n+1):
            item = str(i)
            if i % 3 == 0 and i % 5 == 0:
                item = "FizzBuzz"
            elif i % 3 == 0:
                item = "Fizz"
            elif i % 5 == 0:
                item = "Buzz"
            res.append(item)
        return res
 
if __name__ == "__main__":
    obj = Solution()
    res = obj.fizzBuzz(15)
    print res

"""
@author: Peng

@problem_info:    
    Given n, how many structurally unique BST's (binary search trees) that store values 1...n?

    For example,
        Given n = 3, there are a total of 5 unique BST's.
        
           1         3     3      2      1
            \       /     /      / \      \
             3     2     1      1   3      2
            /     /       \                 \
           2     1         2                 3

"""

class Solution(object):
    
    # solution 1
    def numTrees_1(self, n):
        """
        :idea: the result is "Catalan Number"
        
            set all number is [a1, a2, a3, ..., ak, ..., an], 
            the possible BST number is f(n)
            if the root is ak, then:
                the left sub_BST is [a1, ..., ak-1], 
                the right sub_BST is [ak+1, ..., an], 
            two sub_trees are mutually independent. 
            set their possible BST number set to f(k-1) and f(n-k)
            so :
                f(n) = sum_k { f(k-1)*f(n-k) }
            which is "Catalan Number"
            
        :param n: int, the number of BST nodes
        :return: int, the number of unique BSTs
        """
        fact_n = 1  # n! 
        fact_2n = 1  # (2n)!/(n+1)!
        for i in range(2, n+1): fact_n *= i
        for i in range(n+2,2*n+1): fact_2n *= i
        return int(fact_2n/fact_n)

    # solution 2
    def numTrees_2(self, n):
        """
        :idea: using DP
            the recursion equation is :
                f(n) = sum_k { f(k-1)*f(n-k) }
            here we use a list to store f(i) as i from 1 to n. (set f[0] = 1) 
            
        :param n: int, the number of BST nodes
        :return: int, the number of unique BSTs
        """
        f = []
        f.append(1)
        for i in range(1, n+1) :
            f_i = 0
            for k in range(1, i+1) :
                f_i += f[k-1] * f[i-k]
            f.append(f_i)
        return f[n]

# test code
if __name__ == '__main__':
    s = Solution()
    n = 5
    print("The number of all possible unique BST is: ", s.numTrees_2(n))
    
# - PY131 - #
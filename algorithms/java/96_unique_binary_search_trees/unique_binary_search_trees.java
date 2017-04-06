import java.util.Scanner;

import tree.BinTree;

/**
 * @author Peng
 *
 * Problem Description:
 *      Given n, how many structurally unique BST's (binary search trees) that store values 1...n?
 *    For example,
 *       Given n = 3, there are a total of 5 unique BST's. 
 *       
 *          1         3     3      2      1
 *           \       /     /      / \      \
 *            3     2     1      1   3      2
 *           /     /       \                 \
 *          2     1         2                 3 
 */
public class unique_binary_search_trees {

    /**
     * Solution 1:
     *  derivation as:
     *      set N(n) as the target tree number.
     *          here we count i as the root value of the tree.
     *          so N(i,n) = N(i-1) * N(n-i).
     *              while N(i-1) refers to left subtree count;
     *                    N(n-i) refers to right subtree count;
     *          N(n) = N(1,n) + N(2,n) +...+ N(n,n);
     *      so:
     *      ini:N(0) = 1, N(1) = 1;
     *     then:N(2) = N(1,2) + N(2,2) = (N(0) * N(1)) + (N(1) * N(0)) 
     *               = f(N(0), N(1))
     *          N(3) = N(1,3) + N(2,3) + N(3,3) = (N(0) * N(2)) + (N(1) * N(1)) + (N(2) * N(0))
     *               = f(N(0), N(1), N(2))
     *          ...
     * @param n
     * @return
     */
    public static int numTrees(int n) {
        int [] N = new int[n+1]; //0->n
        N[0] = 1;
        N[1] = 1;
        for(int i = 2; i <= n; i++){
            for(int j = 1; j <= i; j++){
                N[i] += N[j-1] * N[i-j];
            }
        }
        return N[n];
    }
    
    public static void main(String[] args) {
        // creating a binary tree.
        Integer[] data = {1, 2, 3, 4, 5, null, null};
        BinTree bt = new BinTree();
        bt.bTreeRoot = bt.createTree(data, 0, 7);  
        
        Scanner scanner = new Scanner(System.in);
        while(scanner.hasNext()){
            int n = scanner.nextInt();
            System.out.println("the tree number of " + n + " is: " + numTrees(n));
        }
        
        scanner.close();
    }

}

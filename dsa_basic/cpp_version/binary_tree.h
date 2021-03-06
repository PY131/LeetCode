
#include<vector>

struct TreeNode {
    int val;
    TreeNode* left;
    TreeNode* right;
    TreeNode(int x) {
        val = x;
        left = nullptr;
        right = nullptr;
    }
};

class BTree {
  public:
    // rebuild a tree based on pre-order traversal and in-prder traversal
    TreeNode * rebuild_a_tree(std::vector<int> pres, std::vector<int> ins);

    // traversal
    std::vector<int> preorder(TreeNode * root);
    std::vector<int> preorder_iteratively(TreeNode * root);
    std::vector<int> inorder_iteratively(TreeNode * root);
    std::vector<int> postorder_iteratively(TreeNode * root);
    std::vector<int> level(TreeNode * root);
    std::vector<int> level_snake(TreeNode * root);

    // BST中i-th小的节点值
    int kth_node(TreeNode * root, int k);
    // BT中和为某一值的路径
    std::vector<std::vector<int>> find_path_with_sum(TreeNode * root, int sum);

  private:
    TreeNode * rebuild_a_tree(std::vector<int> pres, int lo1, int hi1, 
                              std::vector<int> ins,  int lo2, int hi2);
    void preorder(TreeNode * root, std::vector<int> &res); 
    void add_res(std::vector<int> &res, std::vector<int> &sub_res, bool direction);
};
#include<iostream>
#include<stack>
#include"binary_tree.h"

int find(std::vector<int> array, int target, int lo, int hi) {
    for (int i = lo; i <= hi; i++) {
        if (array[i] == target) {
            return i;
        }
    }
    return -1;
}

TreeNode * BTree::rebuild_a_tree(std::vector<int> pres, std::vector<int> ins) {
    return rebuild_a_tree(pres, 0, pres.size() - 1, ins, 0, ins.size() - 1);
}

TreeNode * BTree::rebuild_a_tree(std::vector<int> pres, int lo1, int hi1, 
                                 std::vector<int> ins,  int lo2, int hi2) {
    if (hi1 < lo1 || hi2 < lo2 || hi1 - lo1 != hi2 - lo2) {
        return nullptr;
    }
    int root_idx = find(ins, pres[lo1], lo2, hi2);
    TreeNode * root = new TreeNode(pres[lo1]);
    int num_l = root_idx - lo2;
    int num_r = hi2 - root_idx;
    root->left = rebuild_a_tree(pres, lo1 + 1, lo1 + num_l, ins, lo2, lo2 + num_l - 1);
    root->right = rebuild_a_tree(pres, hi1 - num_r + 1, hi1, ins, hi2 - num_r + 1, hi2);
    return root;                 
}

std::vector<int> BTree::preorder(TreeNode * root) {
    std::vector<int> res;
    preorder(root, res);
    return res;
}

void BTree::preorder(TreeNode * root, std::vector<int> & res) {
    if (!root) {
        return;
    }
    res.push_back(root->val);
    preorder(root->left, res);
    preorder(root->right, res);
}

std::vector<int> BTree::preorder_iteratively(TreeNode * root) {
    std::vector<int> res;
    std::stack<TreeNode *> S;
    if (root) {
        S.push(root);
    }
    while (!S.empty()) {
        TreeNode * p = S.top();
        S.pop();
        res.push_back(p->val);
        if (p->right) S.push(p->right);
        if (p->left) S.push(p->left);
    }
    return res;
}

void go_along_left_branch(TreeNode * p, std::stack<TreeNode *> &S) {
    while (p) {
        S.push(p);
        p = p->left;
    }
}

std::vector<int> BTree::inorder_iteratively(TreeNode * root) {
    std::stack<TreeNode *> S;
    std::vector<int> res;
    TreeNode * p = root;
    while (true) {
        go_along_left_branch(p, S);
        if (S.empty()) break;
        p = S.top();
        S.pop();
        res.push_back(p->val);
        p = p->right;
    }
    return res;
}

std::vector<int> BTree::postorder_iteratively(TreeNode * root) {
    std::vector<int> res;
    std::stack<TreeNode *> S;
    std::stack<int> tmp;
    if (root) {
        S.push(root);
    }
    while (!S.empty()) {
        TreeNode * p = S.top();
        S.pop();
        tmp.push(p->val);
        if (p->left) S.push(p->left);
        if (p->right) S.push(p->right);
    }
    while (!tmp.empty()) {
        res.push_back(tmp.top());
        tmp.pop();
    }
    return res;
}

std::vector<int> BTree::level(TreeNode * root) {
    std::vector<int> res;
    std::vector<TreeNode *> cur_layer_nodes;
    if (root) {
        cur_layer_nodes.push_back(root);
    }
    while (cur_layer_nodes.size() > 0) {
        std::vector<TreeNode *> next_layer_nodes;
        for (TreeNode * p: cur_layer_nodes) {
            res.push_back(p->val);
            if (p->left) next_layer_nodes.push_back(p->left);
            if (p->right) next_layer_nodes.push_back(p->right);
        }
        cur_layer_nodes = next_layer_nodes;
    }
    return res;
}

void BTree::add_res(std::vector<int> &res, std::vector<int> &sub_res, bool direction) {
    for (size_t i = 0; i < sub_res.size(); i++) {
        size_t idx = i;
        if (direction == true) {
            idx = sub_res.size() - 1 - i;
        }
        res.push_back(sub_res[idx]);
    }
}

std::vector<int> BTree::level_snake(TreeNode * root) {
    std::vector<int> res;
    std::vector<TreeNode *> cur_layer_nodes;
    if (root) {
        cur_layer_nodes.push_back(root);
    }
    bool direction = false;  // direction: false: --> , true: <--
    while (cur_layer_nodes.size() > 0) {
        std::vector<TreeNode *> next_layer_nodes;
        std::vector<int> res_tmp;
        for (TreeNode * p: cur_layer_nodes) {
            res_tmp.push_back(p->val);
            if (p->left) next_layer_nodes.push_back(p->left);
            if (p->right) next_layer_nodes.push_back(p->right);
        }
        cur_layer_nodes = next_layer_nodes;
        add_res(res, res_tmp, direction);
        direction = !direction;
    }
    return res;
}

void find_in_pre_traversal(TreeNode * root, std::vector<int> &pres, int k) {
    if (root) {
        find_in_pre_traversal(root->left, pres, k);
        pres.push_back(root->val);
        if (pres.size() == k) {
            return;
        } 
        find_in_pre_traversal(root->right, pres, k);
    }
}

int BTree::kth_node(TreeNode * root, int k) {
    std::vector<int> pres;
    find_in_pre_traversal(root, pres, k);
    return pres[k - 1];
}

void find_path_with_sum_dfs(TreeNode * root, int sum, std::vector<std::vector<int>> &res, std::vector<int> &tmp) {
    if (root == nullptr) {
        return;
    }
    tmp.push_back(root->val);
    if (root->val == sum && root->left == nullptr && root->right == nullptr) {
        std::vector<int> new_tmp(tmp.begin(), tmp.end());;
        res.push_back(new_tmp);
    } else {
        find_path_with_sum_dfs(root->left, sum - root->val, res, tmp);
        find_path_with_sum_dfs(root->right, sum - root->val, res, tmp);
    }
    tmp.pop_back();
    return;
}

std::vector<std::vector<int>> BTree::find_path_with_sum(TreeNode * root, int sum) {
    std::vector<std::vector<int>> res;
    std::vector<int> tmp;
    find_path_with_sum_dfs(root, sum, res, tmp);
    return res;
}

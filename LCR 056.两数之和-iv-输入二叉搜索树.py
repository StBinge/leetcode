#
# @lc app=leetcode.cn id=LCR 056 lang=python3
# @lcpr version=30204
#
# [LCR 056] 两数之和 IV - 输入二叉搜索树
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        cache=set()
        def dfs(node:TreeNode):
            if not node:
                return False
            if k-node.val in cache:
                return True
            cache.add(node.val)
            return dfs(node.left) or dfs(node.right)

        return dfs(root)
# @lc code=end



#
# @lcpr case=start
# [8,6,10,5,7,9,11]\n12\n
# @lcpr case=end

# @lcpr case=start
# [8,6,10,5,7,9,11]\n22\n
# @lcpr case=end

#


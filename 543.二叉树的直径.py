#
# @lc app=leetcode.cn id=543 lang=python3
#
# [543] 二叉树的直径
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ret=0
        def dfs(node:TreeNode):
            nonlocal ret
            if not node:
                return 0
            l=dfs(node.left)
            r=dfs(node.right)
            ret=max(ret,l+r)
            return max(l,r)+1
        dfs(root)
        return ret
# @lc code=end

assert Solution().diameterOfBinaryTree(TreeNode.build([1,2,3,4,5]))==3
assert Solution().diameterOfBinaryTree(TreeNode.build([1,2]))==1
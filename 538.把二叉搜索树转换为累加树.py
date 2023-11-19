#
# @lc app=leetcode.cn id=538 lang=python3
#
# [538] 把二叉搜索树转换为累加树
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
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        pre_sum=0
        def traverse(node:TreeNode):
            nonlocal pre_sum
            if not node:
                return
            traverse(node.right)
            pre_sum+=node.val
            node.val=pre_sum
            traverse(node.left)
        traverse(root)
        return root
# @lc code=end


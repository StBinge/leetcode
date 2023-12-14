#
# @lc app=leetcode.cn id=897 lang=python3
#
# [897] 递增顺序搜索树
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
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy=TreeNode(0)
        cur=dummy
        def traverse(node:TreeNode):
            nonlocal cur
            if not node:
                return
            traverse(node.left)
            cur.right=node
            node.left=None
            cur=node
            traverse(node.right)
        traverse(root)
        return dummy.right

# @lc code=end


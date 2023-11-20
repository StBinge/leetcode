#
# @lc app=leetcode.cn id=653 lang=python3
#
# [653] 两数之和 IV - 输入二叉搜索树
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
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        vals=set()
        found=False
        def traverse(root:TreeNode):
            nonlocal found
            if found:
                return
            if not root:
                return
            if k-root.val in vals:
                found=True
                return
            vals.add(root.val)
            traverse(root.left)
            traverse(root.right)
        traverse(root)
        return found
            
# @lc code=end


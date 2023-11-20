#
# @lc app=leetcode.cn id=563 lang=python3
#
# [563] 二叉树的坡度
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
    def findTilt(self, root: Optional[TreeNode]) -> int:
        ret=0
        def traverse(root:TreeNode):
            nonlocal ret
            if not root:
                return 0
            sum_left=traverse(root.left)
            sum_right=traverse(root.right)
            ret+=abs(sum_left-sum_right)
            return sum_left+sum_right+root.val
        traverse(root)
        return ret
# @lc code=end


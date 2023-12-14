#
# @lc app=leetcode.cn id=965 lang=python3
#
# [965] 单值二叉树
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
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if root.left and root.left.val!=root.val:
            return False
        if root.right and root.right.val!=root.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
# @lc code=end
root=TreeNode.build('[2,2,2,5,2]')
assert Solution().isUnivalTree(root)==False
root=TreeNode.build('[1,1,1,1,1,null,1]')
assert Solution().isUnivalTree(root)

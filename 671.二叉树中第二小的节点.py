#
# @lc app=leetcode.cn id=671 lang=python3
#
# [671] 二叉树中第二小的节点
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
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        def find_min(root:TreeNode,low:int):
            if not root:
                return -1
            if root.val>low:
                return root.val
            left=find_min(root.left,low)
            right=find_min(root.right,low)
            if left<0:
                return right
            if right<0:
                return left
            return min(left,right)
        return find_min(root,root.val)
# @lc code=end
assert Solution().findSecondMinimumValue(TreeNode.build([2,2,2]))==-1

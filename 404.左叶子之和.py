#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#
from typing import *
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        # ret=0
        def traverse(head:TreeNode,is_left:bool):
            if not head.left and not head.right:
                return head.val if is_left else 0
            sum=0
            if head.left:
                sum+=traverse(head.left,True)
            if head.right:
                sum+=traverse(head.right,False)
            return sum
        return traverse(root,False)
            
# @lc code=end


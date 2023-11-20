#
# @lc app=leetcode.cn id=701 lang=python3
#
# [701] 二叉搜索树中的插入操作
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
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)
        cur=root
        while cur:
            if val<cur.val:
                if not cur.left:
                    cur.left=TreeNode(val)
                    return root
                cur=cur.left
            else:
                if not cur.right:
                    cur.right=TreeNode(val)
                    return root
                cur=cur.right
# @lc code=end


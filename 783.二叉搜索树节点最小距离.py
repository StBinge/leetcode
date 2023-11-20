#
# @lc app=leetcode.cn id=783 lang=python3
#
# [783] 二叉搜索树节点最小距离
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
    def minDiffInBST(self, root: Optional[TreeNode]) -> int:
        vals=[]
        def traverse(node):
            if not node:
                return
            traverse(node.left)
            vals.append(node.val)
            traverse(node.right)
        traverse(root)
        ret=10**5
        for i in range(1,len(vals)):
            ret=min(ret,vals[i]-vals[i-1])
            if ret==0:
                return 0
        return ret
# @lc code=end


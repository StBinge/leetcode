#
# @lc app=leetcode.cn id=1372 lang=python3
#
# [1372] 二叉树中的最长交错路径
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
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        ret=0
        def dfs(node:TreeNode,dir,length):
            if not node:
                return
            nonlocal ret
            ret=max(ret,length)
            if dir=='l':
                dfs(node.left,'r',length+1)
                dfs(node.right,'l',1)
            if dir=='r':
                dfs(node.right,'l',length+1)
                dfs(node.left,'r',1)
        dfs(root,'l',0)
        dfs(root,'r',0)
        return ret
# @lc code=end
assert Solution().longestZigZag(TreeNode.build('[1,1,1,null,1,null,null,1,1,null,1]'))==4
assert Solution().longestZigZag(TreeNode.build('[1,null,1,1,1,null,null,1,1,null,1,null,null,null,1,null,1]'))==3

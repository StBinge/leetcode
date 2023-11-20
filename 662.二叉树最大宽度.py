#
# @lc app=leetcode.cn id=662 lang=python3
#
# [662] 二叉树最大宽度
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
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        queue=[[root,0]]
        ret=0
        while queue:  
            ret=max(ret,queue[-1][1]-queue[0][1]+1)
            next_level=[]
            for node,idx in queue:
                if node.left:
                    next_level.append([node.left,idx*2+1])
                if node.right:
                    next_level.append([node.right,idx*2+2])
            queue=next_level
        return ret
# @lc code=end


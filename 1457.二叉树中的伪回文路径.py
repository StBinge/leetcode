#
# @lc app=leetcode.cn id=1457 lang=python3
#
# [1457] 二叉树中的伪回文路径
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
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:

        def travers(node:TreeNode,mask):
            if not node:
                return 0
            mask^=1<<node.val
            
            if node.left is node.right:
                return int(mask & (mask-1) ==0)
            return travers(node.left,mask)+travers(node.right,mask)
        return travers(root,0)
    

# @lc code=end

assert Solution().pseudoPalindromicPaths(TreeNode.build('[9]'))==1
assert Solution().pseudoPalindromicPaths(TreeNode.build('[2,3,1,3,1,null,1]'))==2
assert Solution().pseudoPalindromicPaths(TreeNode.build('[2,1,1,1,3,null,null,null,null,null,1]'))==1
#
# @lc app=leetcode.cn id=814 lang=python3
#
# [814] 二叉树剪枝
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
    def pruneTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        root.left=self.pruneTree(root.left)
        root.right=self.pruneTree(root.right)
        if not root.left and not root.right and root.val==0:
            return None
        return root
# @lc code=end
root=TreeNode.build('[1,null,0,0,1]')
assert Solution().pruneTree(root).to_str()=='[1,null,0,null,1]'
root=TreeNode.build('[1,0,1,0,0,0,1]')
ret=Solution().pruneTree(root)

pass

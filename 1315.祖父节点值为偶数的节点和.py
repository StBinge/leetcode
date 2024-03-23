#
# @lc app=leetcode.cn id=1315 lang=python3
#
# [1315] 祖父节点值为偶数的节点和
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
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        ret=0
        def traverse(node:TreeNode,par,parpar):
            nonlocal ret
            if not node:
                return
            if parpar & 1==0:
                ret+=node.val
            traverse(node.left,node.val,par)
            traverse(node.right,node.val,par)
        traverse(root,1,1)
        return ret
# @lc code=end
assert Solution().sumEvenGrandparent(TreeNode.build('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'))==18

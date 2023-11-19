#
# @lc app=leetcode.cn id=687 lang=python3
#
# [687] 最长同值路径
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
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        
        ret=0
        def traverse(node:TreeNode):
            nonlocal ret
            if not node:
                return 0
            left=traverse(node.left)
            right=traverse(node.right)
            left1=left+1 if node.left and node.left.val==node.val else 0
            right1=right+1 if node.right and node.right.val==node.val else 0
            ret=max(ret,left1+right1)
            return max(left1,right1)
        traverse(root)
        return ret
# @lc code=end
root=TreeNode.build([1,4,5,4,4,5])
assert Solution().longestUnivaluePath(root)==2

root=TreeNode.build([5,4,5,1,1,5])
assert Solution().longestUnivaluePath(root)==2

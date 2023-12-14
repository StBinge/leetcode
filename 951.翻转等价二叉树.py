#
# @lc app=leetcode.cn id=951 lang=python3
#
# [951] 翻转等价二叉树
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
    def flipEquiv(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        if not root1 and not root2:
            return True
        if root1 and root2:
            if root1.val != root2.val:
                return False
            return (self.flipEquiv(root1.left,root2.left) and self.flipEquiv(root1.right,root2.right) )or (self.flipEquiv(root1.right,root2.left) and self.flipEquiv(root1.left,root2.right))
        return False
# @lc code=end
root1=TreeNode.build('[]')
root2=TreeNode.build('[1]')
assert Solution().flipEquiv(root1,root2)==False
root1=TreeNode.build('[]')
root2=TreeNode.build('[]')
assert Solution().flipEquiv(root1,root2)
root1=TreeNode.build('[1,2,3,4,5,6,null,null,null,7,8]')
root2=TreeNode.build('[1,3,2,null,6,4,5,null,null,null,null,8,7]')
assert Solution().flipEquiv(root1,root2)

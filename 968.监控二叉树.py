#
# @lc app=leetcode.cn id=968 lang=python3
#
# [968] 监控二叉树
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
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        # not cover 0
        # cover_not_place 1
        # cover_place 2
        count=0
        def dfs(root:TreeNode):
            nonlocal count
            if not root:
                return 1
            if not root.left and not root.right:
                return 0
            left=dfs(root.left)
            right=dfs(root.right)

            if left==0 or right==0:
                count+=1
                return 2
            if left==2 or right==2:
                return 1
            return 0
        
        if dfs(root)==0:
            return count+1
        return count


# @lc code=end
root = TreeNode.build("[0,0,null,0,null,0,null,null,0]")
assert Solution().minCameraCover(root) == 2

root = TreeNode.build("[0,0,null,0,0]")
assert Solution().minCameraCover(root) == 1

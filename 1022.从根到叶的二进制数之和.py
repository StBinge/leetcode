#
# @lc app=leetcode.cn id=1022 lang=python3
#
# [1022] 从根到叶的二进制数之和
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
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        q=[[0,root]]
        ret=0
        while q:
            cur,node=q.pop()
            cur=(cur<<1)+node.val
            if not node.left and not node.right:
                ret+=cur
                continue
            if node.left:
                q.append([cur,node.left])
            if node.right:
                q.append([cur,node.right])
        return ret
# @lc code=end
assert Solution().sumRootToLeaf(TreeNode.build([0]))==0
root = [1,0,1,0,1,0,1]
assert Solution().sumRootToLeaf(TreeNode.build(root))==22

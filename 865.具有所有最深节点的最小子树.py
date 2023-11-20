#
# @lc app=leetcode.cn id=865 lang=python3
#
# [865] 具有所有最深节点的最小子树
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
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        def dfs(node:TreeNode):
            if not node:
                return None,0
            L=dfs(node.left)
            R=dfs(node.right)
            if L[1]>R[1]:
                return L[0],L[1]+1
            if L[1]<R[1]:
                return R[0],R[1]+1
            return node,L[1]+1
        return dfs(root)[0]
# @lc code=end
root=TreeNode.build('[3,5,1,6,2,0,8,null,null,7,4]')
ret=Solution().subtreeWithAllDeepest(root).print()
ret=Solution().subtreeWithAllDeepest(TreeNode(1)).print()
ret=Solution().subtreeWithAllDeepest(TreeNode.build('[0,1,3,null,2]')).print()
pass
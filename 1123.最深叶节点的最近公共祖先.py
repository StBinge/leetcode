#
# @lc app=leetcode.cn id=1123 lang=python3
#
# [1123] 最深叶节点的最近公共祖先
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
    def lcaDeepestLeaves(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        def dfs(node:TreeNode):
            if not node:
                return 0,None
            d1,lca1=dfs(node.left)
            d2,lca2=dfs(node.right)
            if d1>d2:
                return d1+1,lca1
            if d2>d1:
                return d2+1,lca2
            if d1==d2:
                return d1+1,node
        return dfs(root)[1]
        
# @lc code=end
assert Solution().lcaDeepestLeaves(TreeNode.build('[0,1,3,null,2]')).to_str()=='[2]'

root = [1]
assert Solution().lcaDeepestLeaves(TreeNode.build(root)).to_str()=='[1]'

root = '[3,5,1,6,2,0,8,null,null,7,4]'
assert Solution().lcaDeepestLeaves(TreeNode.build(root)).to_str()=='[2,7,4]'
#
# @lc app=leetcode.cn id=1382 lang=python3
#
# [1382] 将二叉搜索树变平衡
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
    def balanceBST(self, root: TreeNode) -> TreeNode:
        nodes=[]
        def traverse(node:TreeNode):
            if not node:
                return
            traverse(node.left)
            nodes.append(node)
            traverse(node.right)
        
        def build(l,r):
            if l>r:
                return None
            mid=(l+r)>>1
            node=nodes[mid]
            node.left=build(l,mid-1)
            node.right=build(mid+1,r)
            return node
        traverse(root)
        return build(0,len(nodes)-1)
# @lc code=end
Solution().balanceBST(TreeNode.build('[1,null,2,null,3,null,4]')).print()

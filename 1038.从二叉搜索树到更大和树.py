#
# @lc app=leetcode.cn id=1038 lang=python3
#
# [1038] 从二叉搜索树到更大和树
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
    def bstToGst(self, root: TreeNode) -> TreeNode:
        s=0
        
        def add_right(node:TreeNode):
            nonlocal s
            if not node:
                return
            add_right(node.right)
            s+=node.val
            node.val=s
            add_right(node.left)
        
        add_right(root)
        return root

# @lc code=end
root='[4,1,6,0,2,5,7,null,null,null,3,null,null,null,8]'
assert Solution().bstToGst(TreeNode.build(root)).to_str()=='[30,36,21,36,35,26,15,null,null,null,33,null,null,null,8]'

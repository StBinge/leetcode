#
# @lc app=leetcode.cn id=1325 lang=python3
#
# [1325] 删除给定值的叶子节点
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
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        def delete(node:TreeNode):
            if not node:
                return None
            node.left=delete(node.left)
            node.right=delete(node.right)
            if not node.left and not node.right and node.val==target:
                return None
            return node
        return delete(root)
        
# @lc code=end

assert Solution().removeLeafNodes(TreeNode.build('[1,2,3,2,null,2,4]'),2).to_str()=='[1,null,3,null,4]'
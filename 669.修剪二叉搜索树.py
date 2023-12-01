#
# @lc app=leetcode.cn id=669 lang=python3
#
# [669] 修剪二叉搜索树
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
    def trimBST(self, root: Optional[TreeNode], low: int, high: int) -> Optional[TreeNode]:
        while root and (root.val<low or root.val>high):
            root=root.left if root.val>high else root.right
        if not root:
            return None
        node=root
        while node.left:
            if node.left.val < low:
                node.left=node.left.right
            else:
                node=node.left
        node=root
        while node.right:
            if node.right.val>high:
                node.right=node.right.left
            else:
                node=node.right
        return root
        
        

# @lc code=end
root=TreeNode.build('[1,0,2]')
ret=Solution().trimBST(root,1,2)

root=TreeNode.build('[3,1,4,null,2]')
ret=Solution().trimBST(root,1,2)
pass

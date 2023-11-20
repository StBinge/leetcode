#
# @lc app=leetcode.cn id=450 lang=python3
#
# [450] 删除二叉搜索树中的节点
#

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
from typing import Optional
# @lc code=start
# Definition for a binary tree node.
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        if key<root.val:
            root.left=self.deleteNode(root.left,key)
        elif key>root.val:
            root.right=self.deleteNode(root.right,key)
        elif not root.left or not root.right:
                return root.left if root.left else root.right
        else:
            successor=root.right
            while successor.left:
                successor=successor.left
            successor.right=self.deleteNode(root.right,successor.val)
            successor.left=root.left
            return successor
        return root





        
# @lc code=end

root=TreeNode(5,
            left=TreeNode(3,
                            left=TreeNode(2),
                            right=TreeNode(4)),
            right=TreeNode(6,right=TreeNode(7)))

r=Solution().deleteNode(root,5)
pass
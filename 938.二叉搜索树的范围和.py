#
# @lc app=leetcode.cn id=938 lang=python3
#
# [938] 二叉搜索树的范围和
#
from cv2 import solve
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        if root.val<low:
            return self.rangeSumBST(root.right,low,high)
        if root.val>high:
            return self.rangeSumBST(root.left,low,high)
        return root.val + self.rangeSumBST(root.left,low,high)+self.rangeSumBST(root.right,low,high)
# @lc code=end
root = TreeNode.build('[10,5,15,3,7,13,18,1,null,6]')
low = 6
high = 10
assert Solution().rangeSumBST(root,low,high)==23

root = TreeNode.build('[10,5,15,3,7,null,18]')
low = 7
high = 15
assert Solution().rangeSumBST(root,low,high)==32
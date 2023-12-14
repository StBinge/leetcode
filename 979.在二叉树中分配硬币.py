#
# @lc app=leetcode.cn id=979 lang=python3
#
# [979] 在二叉树中分配硬币
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
    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        ret=0
        def move(node:TreeNode):
            nonlocal ret
            if not node:
                return 0
            left=move(node.left) if node.left else 0
            right=move(node.right) if node.right else 0
            ret+=abs(left)+abs(right)
            return left+right+1-node.val
        move(root)
        return ret
# @lc code=end
root=TreeNode.build([0,3,0])
assert Solution().distributeCoins(root)==3

root=TreeNode.build([3,0,0])
assert Solution().distributeCoins(root)==2



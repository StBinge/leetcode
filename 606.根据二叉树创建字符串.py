#
# @lc app=leetcode.cn id=606 lang=python3
#
# [606] 根据二叉树创建字符串
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
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if not root:
            return ''
        left=self.tree2str(root.left)
        left_str='('+left+')'
        right=self.tree2str(root.right)
        right_str='('+right+')' if right else ''
        return str(root.val)+left_str+right_str if left or right else str(root.val)

# @lc code=end
root=TreeNode(1,
              TreeNode(2,None,TreeNode(4)),
              TreeNode(3))
print(Solution().tree2str(root))

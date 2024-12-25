#
# @lc app=leetcode.cn id=2331 lang=python3
# @lcpr version=30204
#
# [2331] 计算布尔二叉树的值
#
from sbw import *

# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        if not root.left:
            return root.val==1
        left=self.evaluateTree(root.left)
        right=self.evaluateTree(root.right)
        return left | right if root.val==2 else left and right
# @lc code=end



#
# @lcpr case=start
# [2,1,3,null,null,0,1]\n
# @lcpr case=end

# @lcpr case=start
# [0]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=LCR 175 lang=python3
# @lcpr version=30204
#
# [LCR 175] 计算二叉树的深度
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
    def calculateDepth(self, root: Optional[TreeNode]) -> int:
        def depth(node):
            if not node:
                return 0
            left=depth(node.left)
            right=depth(node.right)
            return 1+max(left,right)
        return depth(root)
# @lc code=end



#
# @lcpr case=start
# [1, 2, 2, 3, null, null, 5, 4, null, null, 4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=面试题 04.04 lang=python3
# @lcpr version=30204
#
# [面试题 04.04] 检查平衡性
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
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        def dfs(node:TreeNode):
            if not node:
                return 0
            left=dfs(node.left)
            if left==-1:
                return -1
            right=dfs(node.right)
            if right==-1 or abs(right-left)>1:
                return -1
            return max(left,right)+1
        
        return dfs(root)!=-1
# @lc code=end
assert Solution().isBalanced(TreeNode.build('[1,2,2,3,3,null,null,4,4]')) == False
assert Solution().isBalanced(TreeNode.build('[3,9,20,null,null,15,7]'))



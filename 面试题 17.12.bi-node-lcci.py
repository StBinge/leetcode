#
# @lc app=leetcode.cn id=面试题 17.12 lang=python3
# @lcpr version=30204
#
# [面试题 17.12] BiNode
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
    def convertBiNode(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        head=TreeNode(-1)
        pre=head
        def dfs(node:TreeNode):
            nonlocal pre
            if not node:
                return 
            dfs(node.left)
            pre.right=node
            pre=node
            node.left=None
            dfs(node.right)
        dfs(root)
        return head.right
# @lc code=end



#
# @lcpr case=start
# [4,2,5,1,3,null,6,0]\n
# @lcpr case=end

#


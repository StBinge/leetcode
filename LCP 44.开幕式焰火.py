#
# @lc app=leetcode.cn id=LCP 44 lang=python3
# @lcpr version=30204
#
# [LCP 44] 开幕式焰火
#

from sbw import *
# @lcpr-template-start

# @lcpr-template-end
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    def numColor(self, root: TreeNode) -> int:
        colors=set()
        def dfs(node:TreeNode):
            if not node:
                return
            colors.add(node.val)
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return len(colors)
# @lc code=end



#
# @lcpr case=start
# [1,3,2,1,null,2]`>\n
# @lcpr case=end

# @lcpr case=start
# [3,3,3]`>\n
# @lcpr case=end

#


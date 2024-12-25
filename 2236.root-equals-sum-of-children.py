#
# @lc app=leetcode.cn id=2236 lang=python3
# @lcpr version=30204
#
# [2236] 判断根结点是否等于子结点之和
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
    def checkTree(self, root: Optional[TreeNode]) -> bool:
        return root.val==root.left.val+root.right.val
# @lc code=end



#
# @lcpr case=start
# [10,4,6]\n
# @lcpr case=end

# @lcpr case=start
# [5,3,1]\n
# @lcpr case=end

#

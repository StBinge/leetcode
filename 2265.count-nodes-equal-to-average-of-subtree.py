#
# @lc app=leetcode.cn id=2265 lang=python3
# @lcpr version=30204
#
# [2265] 统计值等于子树平均值的节点数
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
    def averageOfSubtree(self, root: TreeNode) -> int:
        def dfs(root: TreeNode):
            if not root:
                return 0, 0, 0
            left = dfs(root.left)
            right = dfs(root.right)
            s = left[1] + right[1] + root.val
            cnt = left[2] + right[2] + 1
            return left[0] + right[0] + (s // cnt == root.val), s, cnt

        return dfs(root)[0]


# @lc code=end


#
# @lcpr case=start
# [4,8,5,0,1,null,6]\n
# @lcpr case=end

# @lcpr case=start
# [1]\n
# @lcpr case=end

#

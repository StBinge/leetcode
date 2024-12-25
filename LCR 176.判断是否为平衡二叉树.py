#
# @lc app=leetcode.cn id=LCR 176 lang=python3
# @lcpr version=30204
#
# [LCR 176] 判断是否为平衡二叉树
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
        valid=True
        def dfs(node:TreeNode):
            nonlocal valid
            if not node or not valid:
                return 0
            left=dfs(node.left)
            right=dfs(node.right)
            valid=abs(left-right)<2 and valid
            return max(left,right)+1
        dfs(root)
        return valid
# @lc code=end
assert Solution().isBalanced(TreeNode.build('[1,2,3,4,5,null,6,7,null,null,null,null,8]'))==False


#
# @lcpr case=start
# [3,9,20,null,null,15,7]\n
# @lcpr case=end

# @lcpr case=start
# [1,2,2,3,3,null,null,4,4]\n
# @lcpr case=end

#


#
# @lc app=leetcode.cn id=LCR 194 lang=python3
# @lcpr version=30204
#
# [LCR 194] 二叉树的最近公共祖先
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
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if root in [None,p,q]:
            return root
        left=self.lowestCommonAncestor(root.left,p,q)
        right=self.lowestCommonAncestor(root.right,p,q)
        if left and right:
            return root
        return left or right
# @lc code=end
assert Solution().lowestCommonAncestor(TreeNode.build('[3,5,1,6,2,0,8,null,null,7,4]'), TreeNode(5),TreeNode(4)).val==5


#
# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n1\n
# @lcpr case=end

# @lcpr case=start
# [3,5,1,6,2,0,8,null,null,7,4]\n5\n4\n
# @lcpr case=end

#


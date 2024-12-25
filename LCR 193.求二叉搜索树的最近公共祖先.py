#
# @lc app=leetcode.cn id=LCR 193 lang=python3
# @lcpr version=30204
#
# [LCR 193] 二叉搜索树的最近公共祖先
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
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p,q=p.val,q.val
        if p>q:
            p,q=q,p
        while True:
            if p>root.val:
                root=root.right
            elif q<root.val:
                root=root.left
            else:
                return root


    
# @lc code=end
assert Solution().lowestCommonAncestor(TreeNode.build('[6,2,8,0,4,7,9,null,null,3,5]'), TreeNode(2),TreeNode(4)).val==2
assert Solution().lowestCommonAncestor(TreeNode.build('[6,2,8,0,4,7,9,null,null,3,5]'), TreeNode(2),TreeNode(8)).val==6


#
# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n8\n
# @lcpr case=end

# @lcpr case=start
# [6,2,8,0,4,7,9,null,null,3,5]\n2\n4\n
# @lcpr case=end

#


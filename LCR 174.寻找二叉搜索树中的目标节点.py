#
# @lc app=leetcode.cn id=LCR 174 lang=python3
# @lcpr version=30204
#
# [LCR 174] 寻找二叉搜索树中的目标节点
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
    def findTargetNode(self, root: Optional[TreeNode], cnt: int) -> int:
        ret=-1
        # cnt-=1
        def traverse(node:TreeNode):
            nonlocal ret,cnt
            if not node or ret>=0:
                return
            traverse(node.right)
            cnt-=1
            if cnt==0:
                ret=node.val
                return
            traverse(node.left)
        traverse(root)
        return ret
# @lc code=end
assert Solution().findTargetNode(TreeNode.build('[10, 5, 15, 2, 7, null, 20, 1, null, 6, 8]'),4)==8
assert Solution().findTargetNode(TreeNode.build([7, 3, 9, 1, 5]),2)==7


#
# @lcpr case=start
# [7, 3, 9, 1, 5]\n27/ \3   9/ \1   5\n
# @lcpr case=end

# @lcpr case=start
# [10, 5, 15, 2, 7, null, 20, 1, null, 6, 8]\n410/ \5   15/ \    \2   7    20/   / \ 1   6   8\n
# @lcpr case=end

#


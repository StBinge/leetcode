#
# @lc app=leetcode.cn id=1373 lang=python3
#
# [1373] 二叉搜索子树的最大键值和
#
from sbw import *
# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        ret=0
        Max=10**5
        Min=-10**5
        def dfs(node:TreeNode):
            if not node:
                return Max,Min,0
            l_min,l_max,l_s=dfs(node.left)
            r_min,r_max,r_s=dfs(node.right)
            if node.val>l_max and node.val<r_min:
                nonlocal ret
                s=node.val+l_s+r_s
                ret=max(ret,s)
                return min(l_min,node.val),max(r_max,node.val),s
            else:
                return Min,Max,0
        dfs(root)
        return ret
# @lc code=end

assert Solution().maxSumBST(TreeNode.build(' [5,4,8,3,null,6,3]'))==7
assert Solution().maxSumBST(TreeNode.build('[2,1,3]'))==6
assert Solution().maxSumBST(TreeNode.build('[-4,-2,-5]'))==0
assert Solution().maxSumBST(TreeNode.build('[4,3,null,1,2]'))==2
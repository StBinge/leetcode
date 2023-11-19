#
# @lc app=leetcode.cn id=530 lang=python3
#
# [530] 二叉搜索树的最小绝对差
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
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        n=-10**6
        ret=10**7
        def update(node:TreeNode):
            if not node:
                return
            nonlocal n, ret
            val=node.val
            ret=min(ret,val-n)
            n=val
        cur=root
        while cur:
            if not cur.left:
                update(cur)
                cur=cur.right
                continue
            pre=cur.left
            while pre.right and pre.right!=cur:
                pre=pre.right
            
            if not pre.right:
                pre.right=cur
                cur=cur.left
            else:
                pre.right=None
                update(cur)
                cur=cur.right

        return ret
# @lc code=end

assert Solution().getMinimumDifference(TreeNode.build([4,2,6,1,3]))==1
assert Solution().getMinimumDifference(TreeNode.build('[1,0,48,null,null,12,49]'))==1
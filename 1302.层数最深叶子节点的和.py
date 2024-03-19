#
# @lc app=leetcode.cn id=1302 lang=python3
#
# [1302] 层数最深叶子节点的和
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
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=[root]
        while q:
            nxt=[]
            for node in q:
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            if not nxt:
                return sum(node.val for node in q)
            q=nxt
        
# @lc code=end
assert Solution().deepestLeavesSum(TreeNode.build('[6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]'))==19
assert Solution().deepestLeavesSum(TreeNode.build(' [1,2,3,4,5,null,6,7,null,null,null,null,8]'))==15

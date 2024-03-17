#
# @lc app=leetcode.cn id=1448 lang=python3
#
# [1448] 统计二叉树中好节点的数目
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
    def goodNodes(self, root: TreeNode) -> int:
        ret=0
        q=[[root,root.val]]
        while q:
            node,ma=q.pop()
            if node.val>=ma:
                ret+=1
            ma=max(node.val,ma)
            if node.left:
                q.append([node.left,ma])
            if node.right:
                q.append([node.right,ma])
        return ret
# @lc code=end
assert Solution().goodNodes(TreeNode.build('[2,null,4,10,8,null,null,4]'))==4
assert Solution().goodNodes(TreeNode.build('[1]'))==1
assert Solution().goodNodes(TreeNode.build('[3,3,null,4,2]'))==3
assert Solution().goodNodes(TreeNode.build('[3,1,4,3,null,1,5]'))==4
